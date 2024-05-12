from fastapi import APIRouter
from user import RegisterValidator, DeleteUserValidator, EditUserValidator

from database.userservice import edit_user_db, delete_user_db, register_user_db, get_all_users_db, \
    get_exact_user_db

user_router = APIRouter(prefix='/user', tags=['Управление Пользователями'])


# Registerer
@user_router.post('/register')
async def register_user(data: RegisterValidator):
    result = register_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Пользователь есть'}


# Poluchit kakogo to user or all users
@user_router.get('/get-user')
async def get_user(user_id: int = 0):
    if user_id == 0:
        result = get_all_users_db()

        return {'message': result}
    else:
        result = get_exact_user_db(user_id)

        return {'message': result}


@user_router.delete('/delete-user')
async def delete_user(data: DeleteUserValidator):
    result = delete_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': "Пользователь не найден"}


@user_router.put('/edit-data')
async def edit_user(data: EditUserValidator):
    change_data = data.model_dump()

    result = edit_user_db(**change_data)
    if result:
        return {'message': result}
    else:
        return {'message': "Пользователь не найден"}
