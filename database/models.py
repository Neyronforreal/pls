from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(String)
    city = Column(String)
    password = Column(String)
    reg_date = Column(DateTime)


class Service(Base):
    __tablename__ = 'service'
    toy_id = Column(Integer, primary_key=True, autoincrement=True)
    toy_type = Column(String)
    toy_name = Column(String)
    count_toy = Column(Integer)
    toy_price = Column(Float)
    toy_photo = Column(String)
