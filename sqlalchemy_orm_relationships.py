import os

from sqlalchemy.orm import joinedload
import data.db_session as db_session
from data.publisher import Publisher

from data.book import Book
from data.author import Author
from data.book_details import BookDetails
from data.book_author import BookAuthor


def setup_db():
    db_file = os.path.join(os.path.dirname(__file__), 'db', 'Bookstore.sqlite')
    db_session.global_init(db_file)

def create_publisher(name):

    publisher = Publisher()
    publisher.name = name

    return publisher

def create_book(title, isbn, pages, publisher):
    book = Book()
    book.title = title
    book.isbn = isbn
    book.pages = pages
    book.publisher = publisher

    return book


def create_author(first, last):
    author = Author()
    author.first_name = first
    author.last_name = last

    return author

def create_book_details(cover, book):
    details = BookDetails()
    details.book = book
    details.cover = cover

    return details

def create_example_data(ses):
    manning = create_publisher("Manning Publications")

    ses.add(manning)

    # one-to-many
    bookA = create_book('The Mikado Method', '9781617291210', 245, manning)
    ses.add(bookA)


    bookB = create_book('Specification by Example', '9781617290084', 249, manning)
    ses.add(bookB)


    # many-to-many
    authorA = create_author('Ola', 'Ellenestam')

    ses.add(authorA)

    authorB = create_author('Daniela', 'Brolund')
    ses.add(authorB)

    authorC = create_author('Gojko', 'Adzic')
    ses.add(authorC)

    bookA.authors.append(authorA)
    bookA.authors.append(authorB)
    bookB.authors.append(authorC)

    # one-to-one
    detail = create_book_details('477597.jpg', bookA)
    ses.add(detail)

    ses.commit()

    return manning.id, bookA.id, bookB.id

def show_book_and_publisher(publisher_id, ses):
    publisher = ses.query(Publisher).options(joinedload('books')).filter(Publisher.id == publisher_id).first()

    for b in publisher.books:
        print(f'{b.title} published by {b.publisher}')


def show_authors_of_book(bookA_id, bookB_id, ses):
    books = ses.query(Book).options(joinedload('authors')).filter(Book.id.in_([bookA_id, bookB_id])).all()

    for b in books:
        print(b)
        for a in b.authors:
            print(f'\t{a}')

def show_book_details(bookA_id, ses):
    books = ses.query(Book).options(joinedload('details')).filter(Book.id ==bookA_id).all()
    for b in books:
        print(b)
        print(b.details)


if __name__ == '__main__':
    print("\n---setup_db()___\n")
    setup_db()

    print("\n---create session___\n")
    session = db_session.factory()

    print("\n---create_example_data()___\n")
    publisher_id, bookA_id, bookB_id = create_example_data(session)

    print("\n---show_book_and_publisher()___\n")
    show_book_and_publisher(publisher_id, session)

    print("\n---show_authors_of_book()___\n")
    show_authors_of_book(bookA_id, bookB_id, session)

    print("\n---show_book_details() ---\n")
    show_book_details(bookA_id, session)

    print("--- close session ---")
    session.close()









