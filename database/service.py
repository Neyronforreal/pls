from database import get_db
from datetime import datetime
from database.models import Service


def add_toy_db(toy_type, toy_name, count_toy, toy_price):
    with next(get_db()) as db:
        new_toy = Service(toy_type=toy_type, toy_name=toy_name,
                           count_toy=count_toy, toy_price=toy_price)
        db.add(new_toy)
        db.commit()
        return {'message': f'Игрушка успешно добавлена, id - {new_toy.toy_id}'}


def get_all_toys_db():
    db = next(get_db())

    all_toys = db.query(Service).all()

    return all_toys


def get_exact_toy_db(toy_id):
    db = next(get_db())

    toys = db.query(Service).filter_by(toy_id=toy_id).first()

    if toys:
        return {'Игрушка': toys}
    else:
        return 'Такой игрушки нет'


def delete_toy_db(toy_id: int):
    db = next(get_db())

    delete_toy = db.query(Service).filter_by(toy_id=toy_id).first()

    if delete_toy:
        db.delete(delete_toy)
        db.commit()
        return f'Игрушка с айдишником {toy_id} успешно удалена'


def edit_toy_db(toy_id, toy_type, toy_name, count_toy, toy_price):
    db = next(get_db())

    exact_toy = db.query(Service).filter_by(toy_id=toy_id).first()

    if exact_toy:
        if toy_type is not None:
            exact_toy.toy_type = toy_type

        if toy_name is not None:
            exact_toy.toy_name = toy_name

        if count_toy is not None:
            exact_toy.count_toy = count_toy

        if toy_price is not None:
            exact_toy.toy_price = toy_price

        db.commit()
        return {'message': 'Информация об игрушке успешно изменена'}
    else:
        return {'message': 'Не удалось найти игрушку с указанным идентификатором'}


def add_toy_photo_db(toy_photo, toy_id):
    db = next(get_db())

    checker = db.query(Service).filter_by(toy_id=toy_id).first()

    if checker:
        checker.toy_photo = toy_photo

        db.commit()
        return {'message': 'Картинка соотвестувует игрушке'}

    else:
        return {'message': 'Игрушка не найдена'}
