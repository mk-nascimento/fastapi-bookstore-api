from typing import List

from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from bookstore.enums.author_related import Language


class Base(DeclarativeBase): ...


class Author(Base):
    __tablename__ = 'tb_authors'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64), unique=True)
    nationality: Mapped[str] = mapped_column(String(32))
    language: Mapped[Language]

    books: Mapped[List['Book']] = relationship(
        back_populates='author', cascade='all, delete-orphan'
    )


class Book(Base):
    __tablename__ = 'tb_books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str]
    genre: Mapped[str] = mapped_column(String(48))
    publication_year: Mapped[int] = mapped_column(
        Integer, CheckConstraint('LENGTH(publication_date::text) = 4'), nullable=False
    )

    publisher_id: Mapped[int] = mapped_column(ForeignKey('tb_publishers.id'))
    author_id: Mapped[int] = mapped_column(ForeignKey('tb_authors.id'))
    author: Mapped[Author] = relationship(back_populates='books')


class Publisher(Base):
    __tablename__ = 'tb_publishers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32), unique=True)
    country: Mapped[str] = mapped_column(String(72))
    website: Mapped[str] = mapped_column(nullable=True)
