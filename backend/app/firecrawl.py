from firecrawl.firecrawl import FirecrawlApp
from pydantic import BaseModel, Field, create_model
from typing import Dict, List, Optional, Any
import os
from dotenv import load_dotenv
from .models import Column

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

# Initialize FirecrawlApp
app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

def create_extraction_schema(columns: List[Column]) -> dict:
    fields = {}
    for col in columns:
        # Use original column name as field key for consistency
        field_key = col.name.lower().replace(' ', '_')
        fields[field_key] = (str, Field(description=f"Extract information about {col.name} from the webpage"))

    schema_model = create_model('DynamicSchema', **fields)
    schema = schema_model.model_json_schema()

    if "title" in schema:
        del schema["title"]

    print(f"Created extraction schema: {schema}")
    return schema

async def extract_data(website: str, columns: List[Column]) -> Dict[str, str]:
    try:
        print(f"\nStarting extraction for {website}")
        schema = create_extraction_schema(columns)
        print(f"Using columns: {[col.name for col in columns]}")

        # Ensure website has http:// or https:// prefix
        if not website.startswith(('http://', 'https://')):
            website = 'https://' + website

        print("Making Firecrawl API call...")
        data = app.scrape_url(website, {
            'formats': ['extract'],
            'extract': {
                'schema': schema,
                'systemPrompt': 'Extract the requested information from the webpage. Be precise and concise.'
            }
        })

        print(f"Raw Firecrawl response: {data}")

        # Map the extracted data back to original column names
        extracted_data = {}
        raw_data = data.get("extract", {})
        for col in columns:
            field_key = col.name.lower().replace(' ', '_')
            extracted_data[col.name] = raw_data.get(field_key, "N/A")

        print(f"Final extracted data: {extracted_data}")
        return extracted_data

    except Exception as e:
        print(f"Extraction error for {website}: {str(e)}")
        print(f"Full error details: {type(e).__name__}: {str(e)}")
        return {col.name: "N/A" for col in columns}
