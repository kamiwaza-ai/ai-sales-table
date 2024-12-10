from app.firecrawl import extract_data
from app.models import Column
import asyncio

async def test_extraction():
    # Test columns
    columns = [
        Column(name="Company Name"),
        Column(name="Employee Count"),
        Column(name="Revenue Range")
    ]

    # Test extraction with kamiwaza.ai
    result = await extract_data("https://www.kamiwaza.ai", columns)
    print("Extraction result:", result)

    # Test error handling with invalid URL
    error_result = await extract_data("https://invalid.url.test", columns)
    print("Error handling result:", error_result)

if __name__ == "__main__":
    asyncio.run(test_extraction())
