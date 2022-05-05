import sqlalchemy as sa
from .modelbase import ModelBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Publisher(ModelBase):

    __tablename__ = 'Publisher'

    id = sa.Column('Id', sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column('Name', sa.String, nullable=False, index=True)
    books = sa.orm.relationship('Book', back_populates='publisher')

    def __repr__(self):
        return f'<Publisher {self.id} ({self.name})>'
