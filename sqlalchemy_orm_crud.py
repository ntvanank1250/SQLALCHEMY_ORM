import os
import data.db_session as db_session

from data.employee import Employee


def setup_db():
    db_file = os.path.join(os.path.dirname(__file__),'db', 'Northwind_small.sqlite')
    db_session.global_init(db_file)

def add_employee(ses):
    employee=Employee()

    employee.last_name="King"
    employee.first_name="Robert"
    employee.birth_date="1990-05-29"

    ses.add(employee)
    ses.commit()
    print(employee)

    return employee.id

def load_employee(id,ses):
    employee=ses.query(Employee).filter(Employee.id==id).first()
    print(employee)

def update_employee(id,ses):
    employee = ses.query(Employee).filter(Employee.id == id).first()
    print(employee)
    employee.last_name = "Lord"

    ses.commit()
    print(employee)

def delete_employee(id,ses):
    employee = ses.query(Employee).filter(Employee.id == id).first()
    print(employee)

    ses.delete(employee)
    ses.commit()

if __name__=='__main__':
    print("----- setup_db() ----")
    setup_db()

    print("----- create session() ----")
    session=db_session.factory()

    print("----- add_employee() ----")
    id=add_employee(session)

    print("----- update_employee() ----")
    update_employee(id, session)

    print("----- delete_employee() ----")
    delete_employee(id, session)
    load_employee(id, session)

    print("----- close session() ----")
    session.close()

    print("----- create session() ----")
    session = db_session.factory()



