from pydantic import BaseModel, Field, field_validator, field_serializer, ConfigDict
from bson.objectid import ObjectId
from typing import Optional

class DataChunk(BaseModel):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    chunk_text: str = Field(default=None ,min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(default=None, gt=0)
    chunk_project_id: ObjectId

    @field_serializer
    def serialize_id(self, value: Optional[ObjectId]) -> Optional[str]:
        return str(value) if value else None
    
    

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True
    )