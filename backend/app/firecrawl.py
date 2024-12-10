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
        # Use lowercase column name as the field key
        field_key = col.name.lower().replace(" ", "_")
        fields[field_key] = (str, Field(description=f"Extract {col.name} from the webpage"))

    schema_model = create_model('DynamicSchema', **fields)
    schema = schema_model.model_json_schema()

    if "title" in schema:
        del schema["title"]

    return schema

async def extract_data(website: str, columns: List[Column]) -> Dict[str, str]:
    try:
        schema = create_extraction_schema(columns)

        data = app.scrape_url(website, {
            'formats': ['extract'],
            'extract': {
                'schema': schema,
                'systemPrompt': """You are an expert at extracting company information from websites.
                For 'Company Name', extract the official name of the company.
                For 'Mission', extract the company's mission statement or main purpose."""
            }
        })

        # Convert the extracted data to match column names exactly
        extracted_data = {}
        raw_data = data.get("extract", {})
        for col in columns:
            field_key = col.name.lower().replace(" ", "_")
            # Use original column name as key to preserve case
            extracted_data[col.name] = raw_data.get(field_key, "N/A")

        return extracted_data

    except Exception as e:
        print(f"Extraction error for {website}: {str(e)}")
        return {col.name: "N/A" for col in columns}
