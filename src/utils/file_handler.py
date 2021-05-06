from book import Book

commands = {
    'new book': 'create a new book',
    'remove book': 'remove a book',
    'list': 'list the books',
    'export <filepath_here>': 'export the book list creating a new file)',
    'import <filepath_here>': 'import a file into the book list'
}


def write_file(path: str, bookList: list[Book]) -> None:
    try:
        file = open(path, mode='x')
        for book in bookList:
            file.write(
                f'{book.name},{book.author},{book.edition}, {book.currentChapter}')
        file.flush()
        file.close()
    except FileExistsError:
        print('[ERR::FILE_EXISTIS] File with that path already existis')


def read_file(path):
    imported_book_list = list()
    try:
        file = open(path, 'r')

        for line in file:
            data = line.split(',')
            print(data)
            book = Book(data[0], data[1], data[2], data[3])
            imported_book_list.append(book)

        return imported_book_list
    except FileNotFoundError:
        print('File does not exits!')
    except Exception:
        print('[ERR::PARSING_FILE] Invalid file format.')
