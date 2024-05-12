from pydantic import BaseModel


# Валидатор для регистрации
class RegisterValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    city: str
    password: str


class DeleteUserValidator(BaseModel):
    id: int


# Валидатор для изменения пользователя
class EditUserValidator(BaseModel):
    id: int
    phone_number: str
    email: str
    password: str
    city: str
# нужно сделать проверку юзера а уже потои рарешить ему узменение его данных
