from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from bookstore.api.main import router
from bookstore.core.deps import origins

app = FastAPI()
app.include_router(router)

HTTP_200, HTTP_307 = status.HTTP_200_OK, status.HTTP_307_TEMPORARY_REDIRECT
allows = dict(allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.add_middleware(CORSMiddleware, allow_origins=origins, **allows)


@app.get('/health', status_code=HTTP_307, include_in_schema=False)
def health():
    return RedirectResponse(url='/')


@app.get('/', status_code=HTTP_200, include_in_schema=False)
def index(): ...
