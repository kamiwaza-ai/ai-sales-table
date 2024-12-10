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

## Core Features

1. **Dynamic Data Grid**
   - First column for website URLs
   - Ability to add new columns representing different data points to extract
   - Automatic data population using Firecrawl

2. **Automated Extraction**
   - Each new column addition triggers Firecrawl jobs
   - Schema-based extraction for structured data
   - Real-time population of results

3. **Basic Error Handling**
   - Display status of extraction attempts
   - Allow manual override for failed extractions

## Technical Architecture

### Frontend (React)
- Single page application with a dynamic data grid
- Built using React with TypeScript for type safety
- Uses AG Grid for the interactive data table
- Simple state management with React Context or Redux
- Real-time updates using WebSocket connection to backend

### Backend (FastAPI)
- FastAPI server handling API requests
- Asynchronous processing of Firecrawl requests
- Basic in-memory caching for recent extractions
- WebSocket support for real-time updates
- SQLite database for storing extraction results

### API Endpoints

```
POST /api/columns
- Add a new column to extract
- Triggers extraction jobs for all rows

POST /api/rows
- Add a new row (website) to analyze
- Triggers extraction for all existing columns

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

class ExtractionJob(BaseModel):
    row_id: str
    column_id: str
    status: str
    result: Optional[str]
```

## Implementation Plan

### 1. Backend Setup
1. Initialize FastAPI project with proper directory structure
2. Set up database models and migrations
3. Implement Firecrawl integration service
4. Create API endpoints for CRUD operations
5. Add WebSocket support for real-time updates
6. Implement basic caching mechanism

### 2. Frontend Setup
1. Create React project with TypeScript
2. Set up AG Grid component
3. Implement column addition UI
4. Create WebSocket connection handler
5. Add basic error handling and loading states

### 3. Integration
1. Connect frontend to backend API endpoints
2. Implement real-time updates
3. Add error handling and retry logic
4. Test end-to-end functionality

## TODO List

### Backend Tasks
- [ ] Set up FastAPI project structure
  ```
  backend/
  ├── app/
  │   ├── main.py
  │   ├── api/
  │   │   └── endpoints/
  │   ├── core/
  │   │   └── config.py
  │   ├── db/
  │   │   └── session.py
  │   ├── models/
  │   └── services/
  │       └── firecrawl.py
  └── requirements.txt
  ```
- [ ] Create database models and migrations
- [ ] Implement Firecrawl service wrapper
- [ ] Create CRUD endpoints for columns and rows
- [ ] Add WebSocket support for real-time updates
- [ ] Implement rate limiting for Firecrawl API
- [ ] Add basic caching layer
- [ ] Set up error handling middleware

### Frontend Tasks
- [ ] Initialize React project with TypeScript
  ```
  frontend/
  ├── src/
  │   ├── components/
  │   │   ├── DataGrid.tsx
  │   │   └── ColumnAdder.tsx
  │   ├── services/
  │   │   └── api.ts
  │   ├── hooks/
  │   │   └── useWebSocket.ts
  │   └── App.tsx
  └── package.json
  ```
- [ ] Set up AG Grid component with basic configuration
- [ ] Create column addition interface
- [ ] Implement WebSocket connection handler
- [ ] Add loading states and error handling
- [ ] Create basic styling and layout
- [ ] Implement manual cell editing functionality

### Integration Tasks
- [ ] Connect frontend to backend API
- [ ] Test WebSocket functionality
- [ ] Implement error handling and retries
- [ ] Add loading indicators
- [ ] Test end-to-end extraction flow

## Getting Started

1. Clone the repository
2. Set up your Firecrawl API credentials in `.env`
3. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
4. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```
5. Start the backend server:
   ```bash
   uvicorn app.main:app --reload
   ```
6. Start the frontend development server:
   ```bash
   npm start
   ```

## Documentation & Resources

- [Firecrawl Documentation](https://docs.firecrawl.dev/features/extract)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [AG Grid Documentation](https://www.ag-grid.com/documentation)
- [React Documentation](https://reactjs.org/docs)
