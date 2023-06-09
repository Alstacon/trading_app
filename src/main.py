from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.responses import RedirectResponse

from auth.auth_config import auth_backend, fastapi_users
from auth.schemas import UserCreate, UserRead
from config import REDIS_HOST, REDIS_PORT
from operations.router import router as router_operation
from tasks.router import router as router_tasks
from pages.router import router as router_pages
from chat.router import router as router_chat

app = FastAPI(
    title='Trading App'
)

app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/')
def old():
    return RedirectResponse('/pages/home')


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
app.include_router(
    router_pages,
    # dependencies=[Depends(current_user)]
)
app.include_router(router_chat)

origins = [
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost:3000',
    'http://127.0.0.1:8000'

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['*'],

)


@app.on_event('startup')
async def startup():
    redis = aioredis.from_url(f'redis://{REDIS_HOST}:{REDIS_PORT}', encoding='utf8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
