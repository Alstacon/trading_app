from auth.models import Role
from tests.conftest import client


def test_register(add_role: Role):
    response = client.post('/auth/register', json={
        'email': 'user@example.com',
        'password': 'string',
        'is_active': True,
        'is_superuser': False,
        'is_verified': False,
        'name': 'string',
        'role_id': add_role.id
    })

    assert response.status_code == 201
