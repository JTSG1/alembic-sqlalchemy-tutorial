from sqlalchemy import Column, Integer, String
from persistence.db import Base
from sqlalchemy import  Column, Integer

class Car(Base):

    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String)
    model = Column(String, unique=True, index=True)
    colour = Column(String)