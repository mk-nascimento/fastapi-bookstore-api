from typing import Type, TypeVar

from fastapi import HTTPException, status

from bookstore.core.database import Session

T = TypeVar('T')


def validate_instance(db: Session, model: Type[T], id: int, /) -> T:
    instance = db.get(model, id)
    if not instance:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'{model.__name__} not found')

    return instance


def add_and_refresh(db: Session, instance: Type[T], /):
    db.add(instance)
    db.commit()
    db.refresh(instance)
