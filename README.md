# Sales Research Assistant

A dynamic web-based tool that automates the extraction of company information using Firecrawl's LLM-powered web scraping capabilities.

## Overview

This tool helps sales teams gather structured information about target companies automatically. Users input company website URLs and define the types of information they want to extract (e.g., company name, headquarters location, CEO name). The system automatically scrapes and populates this information using Firecrawl's API.

### Example Use Case

```
| Website             | Company Name | Headquarters | CEO Name |
|--------------------|--------------|--------------|----------|
| www.company1.com   | [auto]       | [auto]      | [auto]   |
| www.company2.com   | [auto]       | [auto]      | [auto]   |
| www.company3.com   | [auto]       | [auto]      | [auto]   |
```

## Technical Architecture

### Frontend (Next.js + Shadcn/UI)
- Simple, modern UI built with Next.js and Shadcn/UI components
- Dynamic data grid for displaying and managing company data
- Real-time updates using WebSocket connection

### Backend (FastAPI)
- FastAPI server handling API requests
- Async processing of Firecrawl requests
- WebSocket support for real-time updates
- Simple SQLite database for storing results

### API Endpoints

```
POST /api/columns
- Add a new column to extract
- Triggers extraction jobs for all rows

POST /api/rows
- Add a new row (website) to analyze
- Triggers extraction for all columns

GET /api/data
- Retrieve current state of the grid

WS /ws/updates
- WebSocket endpoint for real-time updates
```

### Data Models

```python
# Backend Models
class Column(BaseModel):
    id: str
    name: str
    extraction_key: str

class Row(BaseModel):
    id: str
    website: str
    data: Dict[str, Any]
```

## Implementation Plan

### 1. Backend Setup
```
backend/
├── app/
│   ├── main.py          # FastAPI app
│   ├── models.py        # Pydantic models
│   ├── database.py      # SQLite setup
│   └── firecrawl.py     # Firecrawl integration
└── requirements.txt
```

### 2. Frontend Setup
```
frontend/
├── app/
│   ├── page.tsx         # Main page
│   └── layout.tsx       # Layout
├── components/
│   ├── ui/             # Shadcn components
│   ├── data-grid.tsx   # Main grid component
│   └── add-column.tsx  # Column adder
└── lib/
    └── api.ts          # API client
```

## TODO List

### Backend Tasks
- [ ] Set up FastAPI project
- [ ] Create database models
- [ ] Implement Firecrawl integration
- [ ] Create API endpoints
- [ ] Add WebSocket support

### Frontend Tasks
- [ ] Set up Next.js with Shadcn/UI
- [ ] Create main data grid component
- [ ] Implement column addition
- [ ] Add WebSocket connection
- [ ] Style with Shadcn components

## Getting Started

1. Create the Next.js project with Shadcn/UI:
   ```bash
   npx create-next-app@latest
   cd your-app-name
   npx shadcn@latest init
   ```

2. Configure Shadcn/UI:
   - Style: New York
   - Base color: Zinc
   - CSS variables: Yes

3. Install required Shadcn components:
   ```bash
   npx shadcn@latest add table
   npx shadcn@latest add button
   npx shadcn@latest add input
   npx shadcn@latest add dialog
   ```

4. Set up your Firecrawl API key in `.env`:
   ```
   FIRECRAWL_API_KEY=fc-890953c9205244ff8fb885c2623316eb
   ```

5. Install backend dependencies:
   ```bash
   cd backend
   pip install fastapi uvicorn sqlite-utils python-dotenv
   ```

6. Start the development servers:
   ```bash
   # Terminal 1 - Frontend
   npm run dev
   
   # Terminal 2 - Backend
   uvicorn app.main:app --reload
   ```

## Documentation & Resources
- [Firecrawl Documentation](https://docs.firecrawl.dev/features/extract)
- [Shadcn/UI Documentation](https://ui.shadcn.com)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
