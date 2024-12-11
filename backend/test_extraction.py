from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the FirecrawlApp with API key
api_key = os.getenv('FIRECRAWL_API_KEY')
print(f"Using API key: {api_key}")

app = FirecrawlApp(api_key=api_key)

# Create a simple test schema
class ExtractSchema(BaseModel):
    company_name: str = Field(description="Extract the company name from the webpage")
    mission: str = Field(description="Extract the company's mission or main purpose from the webpage")

# Test URL
url = 'www.kamiwaza.ai'

try:
    print(f"\nTesting extraction from {url}")
    print("Using schema:", ExtractSchema.model_json_schema())

    data = app.scrape_url(url, {
        'formats': ['extract'],
        'extract': {
            'schema': ExtractSchema.model_json_schema(),
            'systemPrompt': 'Extract the requested information from the webpage. Be precise and concise.'
        }
    })

    print("\nRaw API response:")
    print(data)

    print("\nExtracted data:")
    print(data.get("extract", {}))

except Exception as e:
    print(f"Error during extraction: {type(e).__name__}: {str(e)}")
