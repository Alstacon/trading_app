import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from operations.models import Operation

from database import get_async_session
from operations.schemas import OperationCreate

router = APIRouter(
    prefix='/operation',
    tags=['Operation']
)


@router.get('/')
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Operation).where(Operation.type == operation_type)
        result = await session.execute(query)
        return result.scalars().all()
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details': None
        })


@router.post('/')
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {
        'status': 'success',
        'data': None,
        'details': None
    }


@router.get('/long_operation')
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return 'Много много данных, которые вычислялись сто лет'
