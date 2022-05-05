import os
import data.db_session as db_session
from data.employee import Employee
from sqlalchemy import or_, and_


def setup_db():
    db_file = os.path.join(os.path.dirname(__file__), 'db', 'Northwind_small.sqlite')
    db_session.global_init(db_file)


def print_result(result):
    for entry in result:
        print(entry)


def query_all(ses):
    for employee in ses.query(Employee):
        print(employee)


def query_equals(ses):
    for employee in ses.query(Employee).filter(Employee.id == 1):
        print(employee)


def query_not_equals(ses):
    for employee in ses.query(Employee).filter(Employee.id != 1):
        print(employee)


def query_greater_than(ses):
    for employee in ses.query(Employee).filter(Employee.id > 5):
        print(employee)


def query_less_than(ses):
    for employee in ses.query(Employee).filter(Employee.id < 3):
        print(employee)


def query_like(ses):
    for employee in ses.query(Employee).filter(Employee.last_name.like("Pe%k")):
        print(employee)


def query_not_like(ses):
    for employee in ses.query(Employee).filter(Employee.last_name.not_like("Pe%k")):
        print(employee)


def query_contains(ses):
    for employee in ses.query(Employee).filter(Employee.last_name.contains("u")):
        print(employee)


def query_startswith(ses):
    for employee in ses.query(Employee).filter(Employee.last_name.startswith("D")):
        print(employee)


def query_endswith(ses):
    for employee in ses.query(Employee).filter(Employee.last_name.endswith("n")):
        print(employee)


def query_in_(ses):
    for employee in ses.query(Employee).filter(Employee.id.in_([1, 2, 3])):
        print(employee)


def query_in_negated(ses):
    for employee in ses.query(Employee).filter(~Employee.id.in_([1, 2, 3])):
        print(employee)


def query_not_in(ses):
    for employee in ses.query(Employee).filter(Employee.id.not_in([1, 2, 3])):
        print(employee)


def query_multiple_filter_in_one(ses):
    for employee in ses.query(Employee).filter(Employee.id == 7, Employee.last_name == "King"):
        print(employee)


def query_and(ses):
    for employee in ses.query(Employee).filter(and_(Employee.id == 7, Employee.last_name == "King")):
        print(employee)


def query_multiple_filter(ses):
    for employee in ses.query(Employee).filter(Employee.id == 7).filter(Employee.last_name == "King"):
        print(employee)


def query_or(ses):
    for employee in ses.query(Employee).filter(or_(Employee.id == 2, Employee.id == 3)):
        print(employee)


def query_with_python_or(ses):
    for employee in ses.query(Employee).filter(Employee.id == 2 | Employee.id == 3):
        print(employee)


def query_with_python_and_fails(ses):
    for employee in ses.query(Employee).filter(Employee.id == 7 & Employee.last_name == "King"):
        print(employee)


if __name__ == '__main__':
    print("----- setup_db() ----")
    setup_db()

    print("----- create session() ----")
    session = db_session.factory()

    print("----- query_all() ----")
    query_all(session)

    print("----- query_equals() ----")
    query_equals(session)

    print("----- query_not_equals() ----")
    query_not_equals(session)

    print("----- query_greater_than() ----")
    query_greater_than(session)

    print("----- query_less_than() ----")
    query_less_than(session)

    print("----- query_like() ----")
    query_like(session)

    print("----- query_not_like() ----")
    query_not_like(session)

    print("----- query_contains() ----")
    query_contains(session)

    print("----- query_startswith() ----")
    query_startswith(session)

    print("----- query_endswith() ----")
    query_endswith(session)

    print("----- query_in_() ----")
    query_in_(session)

    print("----- query_in_negated() ----")
    query_in_negated(session)

    print("----- query_not_in() ----")
    query_not_in(session)

    print("----- query_multiple_filter_in_one() ----")
    query_multiple_filter_in_one(session)

    print("----- query_and_() ----")
    query_and(session)

    print("----- query_multiple_filter() ----")
    query_multiple_filter(session)

    print("----- query_or_() ----")
    query_or(session)

    print("----- close session ----")
    session.close()
