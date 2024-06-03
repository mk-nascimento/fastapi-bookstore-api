from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get('/health', status_code=HTTPStatus.TEMPORARY_REDIRECT, include_in_schema=False)
def health():
    return RedirectResponse(url='/')


@app.get('/', status_code=HTTPStatus.OK, include_in_schema=False)
def index(): ...
