from typing import Optional

from pydantic import BaseModel, ConfigDict, HttpUrl


class PublisherBase(BaseModel):
    name: str
    country: str
    website: Optional[HttpUrl] = None


class PublisherCreate(PublisherBase): ...


class Publisher(PublisherBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            'example': {
                'id': 1,
                'name': 'Tipografia Nacional',
                'country': 'Brazil',
                'website': 'https://www.example.com',
            }
        },
    )
