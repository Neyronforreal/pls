from fastapi import FastAPI
from fastapi import APIRouter, UploadFile, File
from service import AddToysValidator, DeleteToysValidator, EditToysValidator, Image

from typing import List

from database.service import (add_toy_photo_db, edit_toy_db, add_toy_db,
                                      get_exact_toy_db, get_all_toys_db, delete_toy_db)

toy_router = APIRouter(prefix='/toy', tags=['Управление игрушками'])


@toy_router.post('/add-toy')
async def add_toy(data: AddToysValidator):
    result = add_toy_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Такая игрушка уже есть'}


@toy_router.get('/get-toy')
async def get_exact_toy(toy_id: int = 0):
    if toy_id == 0:
        toys = get_all_toys_db()
        return {'toys': toys}
    else:
        toy = get_exact_toy_db(toy_id)
        return {'toy': toy}


@toy_router.delete('/delete-toy')
async def delete_toy(data: DeleteToysValidator):
    result = delete_toy_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Игрушка не найдена'}


@toy_router.put('/edit-toy-info')
async def edit_toy(data: EditToysValidator):
    change_data = data.model_dump()

    result = edit_toy_db(**change_data)
    if result:
        return {'message': result}
    else:
        return {'message': "Игрушка не найдена"}


@toy_router.post('/Add-photo')
async def add_photo(toy_id: int, toy_photo: UploadFile = File(...)):
    with open(f'photo/{toy_photo.filename}', 'wb+') as file:
        photo = await toy_photo.read()
        file.write(photo)

    photo = add_toy_photo_db(toy_id=toy_id, toy_photo=f'/media/{toy_photo.filename}')

    return {'message': {"Картинка для игрушки, все фото": photo}}
