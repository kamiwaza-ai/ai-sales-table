from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class Column(BaseModel):
    id: Optional[str] = None
    name: str

class Row(BaseModel):
    id: Optional[str] = None
    website: str
    data: Dict[str, Any] = Field(default_factory=dict)

class ColumnCreate(BaseModel):
    name: str

class RowCreate(BaseModel):
    website: str
