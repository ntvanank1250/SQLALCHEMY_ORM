import os
from sqlalchemy.orm import joinedload, selectinload
import data.db_session as db_session
from data.publisher import Publisher
from data.book import Book
from data.author import Author
from data.book_author import BookAuthor
from data.book_details import BookDetails

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

def create_publisher_with_3_books(ses):
    manning = create_publisher('Manning Publications')
    ses.add(manning)

    bookA = create_book('The Mikado Method', '9781617291210', 245, manning)
    ses.add(bookA)

    bookB = create_book('Specification by Example', '9781617290084', 249, manning)
    ses.add(bookB)

    bookC = create_book('Python Workout', '9781617295508', 248, manning)
    ses.add(bookC)

    authorA = create_author('Ola', 'Ellenestam')
    ses.add(authorA)

    authorB = create_author('Daniela', 'Brolund')
    ses.add(authorB)

    authorC = create_author('Gojko', 'Adzic')
    ses.add(authorC)

    authorD = create_author('Reuven M', 'Lerner')
    ses.add(authorD)

    bookA.authors.append(authorA)
    bookA.authors.append(authorB)
    bookB.authors.append(authorC)
    bookC.authors.append(authorD)

    ses.commit()
    return manning.id

def lazy_loading_works_while_session_open(publisher_id, ses):
    publisher = ses.query(Publisher).filter(Publisher.id == publisher_id).first()

    print(f'{publisher}')
    for book in publisher.books:
        print(f'\t {book}:')
        for author in book.authors:
            print(f'\t\t {author}')

def lazy_loading_throws_error(publisher_id, ses):
    publisher = ses.query(Publisher).filter(Publisher.id == publisher_id).first()

    print(f'{publisher}')
    for book in publisher.books:
        print(f'\t {book}:')
        for author in book.authors:
            print(f'\t\t {author}')

def eager_loading_joinedload(publisher_id, ses):
    publisher = ses.query(Publisher).options(joinedload('books').joinedload('authors')).filter(Publisher.id == publisher_id).first()

    print(f'{publisher}')
    for book in publisher.books:
        print(f'\t {book}:')
        for author in book.authors:
            print(f'\t\t {author}')

def eager_loading_selectinload(publisher_id, ses):
    publisher = ses.query(Publisher).options(selectinload('books').selectinload('authors')).filter(Publisher.id == publisher_id).first()

    print(f'{publisher}')
    for book in publisher.books:
        print(f'\t {book}:')
        for author in book.authors:
            print(f'\t\t {author}')

if __name__ == '__main__':
    print("\n---setup_db()___\n")
    setup_db()

    print("\n---create session___\n")
    session = db_session.factory()

    print("\n---create_publisher_with_3_books()___\n")
    publisher_id=create_publisher_with_3_books(session)

    print("\n---lazy_loading_throws_error()___\n")
    try:
        lazy_loading_throws_error(publisher_id, session)
    except Exception as error:
        print(f'{type(error)}: {eror}')

    print("\n--eager_loading_joinedload() ---\n")
    eager_loading_joinedload(publisher_id, session)

    print("\n--eager_loading_selectinload() ---\n")
    eager_loading_selectinload(publisher_id, session)

    print("--- close session ---")
    session.close()
















