from typing import List

from fastapi import APIRouter, Query, status
from sqlalchemy import select

from bookstore import models
from bookstore.core.database import Session
from bookstore.schemas.publisher import Publisher, PublisherCreate
from bookstore.utils import add_and_refresh, validate_instance

router = APIRouter(prefix='/publisher')


@router.post('', response_model=Publisher, status_code=status.HTTP_201_CREATED)
def create(*, session: Session, entity: PublisherCreate):
    instance = models.Publisher(**entity.model_dump())

    add_and_refresh(session, instance)
    return instance


@router.get('', response_model=List[Publisher], status_code=status.HTTP_200_OK)
def read(session: Session, skip: int = Query(None), limit: int = Query(None)):
    statement = select(models.Publisher).offset(skip).limit(limit)

    return session.scalars(statement).all()


@router.get('/{id}', response_model=Publisher, status_code=status.HTTP_200_OK)
def read_unique(*, session: Session, id: int):
    return validate_instance(session, models.Publisher, id)


@router.put('/{id}', response_model=Publisher, status_code=status.HTTP_200_OK)
def update(*, session: Session, id: int, entity: PublisherCreate):
    instance = validate_instance(session, models.Publisher, id)

    for k, v in entity.model_dump(exclude_unset=True).items():
        setattr(instance, k, v)

    add_and_refresh(session, instance)
    return instance


@router.delete('/{id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete(*, session: Session, id: int) -> None:
    instance = validate_instance(session, models.Author, id)

    session.delete(instance)
    session.commit()
