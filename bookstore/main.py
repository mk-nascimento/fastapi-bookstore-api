from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from bookstore.api.main import router

app = FastAPI()
app.include_router(router)


@app.get('/health', status_code=HTTPStatus.TEMPORARY_REDIRECT, include_in_schema=False)
def health():
    return RedirectResponse(url='/')


@app.get('/', status_code=HTTPStatus.OK, include_in_schema=False)
def index(): ...
