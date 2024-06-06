from fastapi import APIRouter

from .routers import author, book, publisher

router = APIRouter(prefix='/api/v0')
router.include_router(author.router, tags=['Author'])
router.include_router(book.router, tags=['Book'])
router.include_router(publisher.router, tags=['Publisher'])
