import sqlalchemy as sa

from .modelbase import ModelBase


class Employee(ModelBase):
    __tablename__ = 'Employee'

    id = sa.Column('Id', sa.Integer, primary_key=True, autoincrement=True)
    last_name = sa.Column('LastName', sa.String, nullable=False)
    first_name = sa.Column('FirstName', sa.String, nullable=False)
    birth_date = sa.Column('BirthDate', sa.String)

    __table_args__ = (
        sa.Index('my_index', 'LastName', 'FirstName'),
    )

    def __repr__(self):
        return f'<Employee {self.id} ({self.first_name} {self.last_name}) {self.birth_date}>'