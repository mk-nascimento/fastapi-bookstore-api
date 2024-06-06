from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator


class BookBase(BaseModel):
    title: str
    genre: str
    publication_year: int
    publisher_id: int
    author_id: int

    @field_validator('publication_year')
    @classmethod
    def validate_year(cls, value: int, info: ValidationInfo):
        REQUIRED_LEN = 4
        if not str(value).isnumeric() or len(str(value)) != REQUIRED_LEN:
            raise ValueError(f'{info.field_name} must be numeric of 4 digits')
        return value


class BookCreate(BookBase): ...


class Book(BookBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            'example': {
                'id': 1,
                'title': 'Memórias Póstumas de Brás Cubas',
                'publication_year': 1881,
                'genre': 'romance,fiction',
                'publisher_id': 1,
                'author_id': 1,
            }
        },
    )
