from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SqlSession

from bookstore.core.config import Settings

env = Settings()
engine = create_engine(env.DATABASE_URI)


def get_session():
    with SqlSession(engine) as session:
        yield session


Session = Annotated[SqlSession, Depends(get_session)]
