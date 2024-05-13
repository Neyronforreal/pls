
from database import get_db
from datetime import datetime
from sqlalchemy.orm import Session

from database.models import User


# Rегистрация пользователя
def register_user_db(name, surname, email,
                     phone_number, city, password):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return True

    new_user = User(name=name, surname=surname, email=email, phone_number=phone_number,
                    city=city, password=password, reg_date=datetime.now())
    db.add(new_user)
    db.commit()
    return f'Юзер успешно добвален'


# олучить all пользователей
def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users


# Poluchit opredelennogo usera
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    return exact_user


def delete_user_db(user_id):
    db = next(get_db())

    delete_user = db.query(User).filter_by(user_id=user_id).first()

    db.delete(delete_user)
    db.commit()
    return f'Юзер с {user_id} успешно удален'


def edit_user_db(user_id, phone_number, email, password, city):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if email is not None:
            exact_user.email = email

        if phone_number is not None:
            exact_user.phone_number = phone_number

        if password is not None:
            exact_user.password = password

        if city is not None:
            exact_user.city = city

        db.commit()

        return {'message': 'Информация о пользователе успешно изменена'}

    else:
        return {'message': 'Не удалось найти пользователя с указанным идентификатором'}
