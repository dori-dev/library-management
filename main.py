"""Library Management
"""

from pickle import load, dump
from os import system
from os.path import exists
from sys import exit as exit_


def check_file_exist():
    """Check files exist
    """

    if not exists("users.dat"):
        with open("users.dat", 'wb') as users:
            dump({}, users)

    if not exists("books.dat"):
        with open("books.dat", 'wb') as books:
            dump({}, books)

    if not exists("borrows.dat"):
        with open("borrows.dat", 'wb') as borrows:
            dump({}, borrows)


def add_user():
    """Add new user with
    name, family, father name, nationality code, birthday and user id
    """
    print('Add New User...')

    with open('users.dat', 'rb') as users:
        users_dict = load(users)

    name = input('Name: ').title()
    family = input('Family: ').title()
    father_name = input('Father: ').title()
    code = input('Nationality Code: ')
    birthday = input('Birthday: ')
    user_id = len(users_dict)

    users_dict[user_id] = [
        name,
        family,
        father_name,
        code,
        birthday
    ]

    with open('users.dat', 'wb') as users:
        dump(users_dict, users)

    print(f"User {user_id} added successfully")
    input('Enter To Go Back...')


def add_book():
    """Add new book with
    title, author, subject, year and book id
    """
    print('Add New Book...')

    with open('books.dat', 'rb') as books:
        book_dict = load(books)

    title = input('Title: ').title()
    author = input('Author: ').title()
    subject = input('Subject: ').capitalize()
    year = input('Year: ')
    book_id = len(book_dict)

    book_dict[book_id] = [title, author, subject, year]

    with open('books.dat', 'wb') as books:
        dump(book_dict, books)

    print(f"Book {book_id} added successfully")
    input('Enter To Go Back...')


def search_book():
    """Search the book with title
    """
    print('Search Book...')

    with open('books.dat', 'rb') as books:
        book_dict = load(books)

    title = input('Book Title: ')
    print(book_dict[title.title()])
    input('Enter To Go Back...')


def borrow():
    """Borrow the book with book title and user id
    """
    print("Borrow Book...")

    with open('borrows.dat', 'rb') as borrows:
        borrows_dict = load(borrows)

    user_id = input('User ID: ')
    title = input('Book Title: ')
    borrows_dict[user_id] = title

    with open('borrows.dat', 'wb') as borrows:
        dump(borrows_dict, borrows)

    input('Enter To Go Back...')


def show_all_info():
    """Showing information of users, books and borrows
    """

    users_dict = load(open('users.dat', 'rb'))
    books_dict = load(open('books.dat', 'rb'))
    borrows_dict = load(open('borrows.dat', 'rb'))

    print("------------------------- Users Information -------------------------")
    for user in users_dict:
        data = users_dict[user]
        name, info = data[:2], data[2:]
        print(f"{' '.join(name)}: {', '.join(info)}")
    print()
    print("------------------------- Books Information -------------------------")
    for book in books_dict:
        data = books_dict[book]
        name, info = data[0], data[1:]
        print(f"{name}: {', '.join(info)}")
    print()
    print("------------------------- Borrow Information -------------------------")
    for user_id in borrows_dict:
        book_title = borrows_dict[user_id]
        print(f"User({user_id}): {book_title}")

    print()
    input('Enter To Go Back...')


def clear_screen():
    """clear screen
    """
    system('clear')


MENU_HINT = """1-Add User
2-Add New Book
3-Search Book
4-Borrow
5-Show All Info
0-Exit"""

function_dict = {
    0: exit_,
    1: add_user,
    2: add_book,
    3: search_book,
    4: borrow,
    5: show_all_info
}

choice = 1
while choice != 0:
    clear_screen()
    print(MENU_HINT)
    choice = input("Enter Choice: ")

    while choice not in ("0", "1", "2", "3", "4", "5"):
        print('Just Enter 1, 2, 3, 4, 5 or 0')
        choice = input("Enter Choice: ")

    clear_screen()
    check_file_exist()

    choice = int(choice)
    option = function_dict[choice]
    option()
