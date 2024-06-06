from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from bookstore.enums.author_related import Language
from bookstore.schemas.book import Book


class AuthorBase(BaseModel):
    name: str
    nationality: Optional[str] = None
    language: Language


class AuthorCreate(AuthorBase): ...


class Author(AuthorBase):
    id: int
    books: List[Book] = []

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            'example': {
                'id': 1,
                'name': 'Machado de Assis',
                'nationality': 'Brazilian',
                'language': 'Portuguese',
                'books': [],
            }
        },
    )
