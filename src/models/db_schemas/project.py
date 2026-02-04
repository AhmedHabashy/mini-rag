from pydantic import BaseModel, Field, field_validator, field_serializer, ConfigDict
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    project_id: str = Field(..., min_length=1)



    @field_serializer
    def serialize_id(self, value: Optional[ObjectId]) -> Optional[str]:
        return str(value) if value else None

    @field_validator('project_id')
    @classmethod
    def validate_project_id(cls,value):
        if not value.strip().isascii() or not value.strip().isalnum():
            raise ValueError('Projectid must be alphanumeric')
        return value

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )   