from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi import FastAPI
from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from auth.auth_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate

from operations.router import router as router_operation
from tasks.router import router as router_tasks
from pages.router import router as router_pages

app = FastAPI(
    title='Trading App'
)
app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth',
    tags=['Auth'],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['Auth'],
)

app.include_router(router_operation)
app.include_router(router_tasks)
app.include_router(router_pages)

origins = [
    'http://localhost:8000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
    allow_headers=['Content-Type', 'Set-Cookie', 'Access-Control-Allow-Headers', 'Access-Control-Allow-Origin',
                   'Authorization'], )


@app.on_event('startup')
async def startup():
    redis = aioredis.from_url('redis://localhost', encoding='utf8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
