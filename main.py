from book import Book
import pprint
import utils
bookList = []


def command_handler(command_line: str) -> None:
    parsed_command = command_line.split()
    try:
        if parsed_command[0] == 'new':
            if parsed_command[1] == 'book':
                add_book()

        if parsed_command[0] == 'remove':
            if parsed_command[1] == 'book':
                remove_book()

        if parsed_command[0] == 'list':
            list_books()

        if parsed_command[0] == 'export':
            utils.write_file(parsed_command[1], bookList)

        if parsed_command[0] == 'import':
            import_books(parsed_command[1])

        if parsed_command[0] == 'help':
            pprint.pprint(utils.commands)

    except IndexError:
        print('[ERROR::COMMAND_HANDLER] command invalid! Type "help"',
              'to see the available commands')


def import_books(file_path: str) -> None:
    imported_list = utils.read_file(file_path)
    if imported_list:
        [bookList.append(book) for book in imported_list]


def add_book() -> None:
    name = input("Book's title: ")
    author = input("Book's author: ")
    edition = int(input("Edition: "))
    current_chapter = int(input("Current chapter: "))

    book = Book(name, author, edition, current_chapter)
    bookList.append(book)


def remove_book() -> None:
    print("Choose a book to delete:")
    list_books()
    key = int(input('Type the id of the book: '))
    bookList.pop(key)


def list_books():
    for (key, book) in enumerate(bookList):
        print(60 * '=')
        print(
            f'{key:^4}|{book.name:^20}|{book.author:^20}|{book.edition:^5}|{book.currentChapter:^5}|')
    print(60 * '=')


cmdInput = ''
while cmdInput != 'q':
    cmdInput = input('>>> ')
    command_handler(cmdInput)
