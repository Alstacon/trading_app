from httpx import AsyncClient

from operations.models import Operation


async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post('/operation', json={
        'id': 1,
        'quantity': '25.5',
        'figi': 'figi_CODE',
        'instrument_type': 'bond',
        'date': '2023-02-01T00:00:00',
        'type': 'Выплата купонов',
    })

    assert response.status_code == 200


async def test_get_specific_operations(ac: AsyncClient, add_operation: Operation):
    response = await ac.get('/operation', params={'operation_type': add_operation.type})

    assert response.status_code == 200
