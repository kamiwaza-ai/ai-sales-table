from firecrawl.firecrawl import FirecrawlApp
from pydantic import BaseModel, Field, create_model
from typing import Dict, Optional, List
import os
from dotenv import load_dotenv
from app.models import Column

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

def create_dynamic_schema(columns: List[Column]) -> type:
    """
    Dynamically create a Pydantic model based on column names
    """
    fields = {}
    for col in columns:
        fields[col.extraction_key] = (str, Field(description=f"Extract {col.name}"))

    schema_model = create_model('DynamicSchema', **fields)
    schema = schema_model.model_json_schema()
    if "title" in schema:
        del schema["title"]
    return schema

def test_extraction():
    # Test columns
    columns = [
        Column(name="Company Name"),
        Column(name="Employee Count"),
        Column(name="Revenue Range")
    ]

    print("Created columns with extraction keys:", [col.extraction_key for col in columns])

    # Create schema directly
    schema = create_dynamic_schema(columns)
    print("Schema:", schema)

    # Initialize FirecrawlApp
    app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

    try:
        # Test extraction
        data = app.scrape_url('https://www.apple.com', {
            'formats': ['extract'],
            'extract': {
                'schema': schema
            }
        })

        print("Extraction successful:")
        print(data["extract"])

    except Exception as e:
        print(f"Extraction failed: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    test_extraction()
