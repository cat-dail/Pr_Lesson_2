from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.backend.db import Base
from app.models import *



class Task(Base):
    __tablename__ = "tasks" # Имя таблицы в базе данных
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True) # Уникальный идентификатор
    title = Column(String) # Название категории
    content = Column(String) # Человекочитаемый URL
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False) # Связь с User
    # Определяем отношение "многие к одному"
    slug = Column(String, unique=True, index=True)
    user = relationship('User', back_populates='tasks')


from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))


