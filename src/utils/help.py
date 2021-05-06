commands = {
    'new': {
        'book': 'create a new book'
    },
    'remove book': {
        'book': 'remove a book'
    },
    'list': 'list the books',
    'export': 'export the book list creating a new file, you must pass a file_path',
    'import': 'import a file into the book list, you must pass a file path'
}


def print_help(command: str = None):
    if command is None:
        for (command, desc) in commands.items():
            print(f'{command}: {desc}')
    else:
        try:
            print(f'{command}: {commands[command]}')
        except KeyError:
            print(f'[ERROR:COMMAND_NOT_FOUND]The "{command}" does not exists!')
