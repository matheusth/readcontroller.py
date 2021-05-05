# Reading Controller

## Introduction
This project is a command line tool to help me keep track of my reading, created with the main object of
helping me understand some concepts of the Python Programing.

## Run this project
- **This project requires the Python interpreter to run: https://www.python.org/**

- Clone this repository
```bash
$ git clone --depth 1 $repo_url$
```

- Enter the repository folder and run the `main.py` file:
```bash
$ cd reading-controller
$ python main.py
```
## Commands
- To register just execute the command ``new book`` and the script will ask you for the books information:
example note that `Edition` and `Current chapter` must be a number.
```bash
>>> new book
Book's title: Dummy Title
Book's author: No Author
Edition: 1
Current chapter: 1
```
- To list the books that you can type ``list``:
```bash
>>> list
============================================================
 0  |    Dummy title     |     an author      |  1  |  1  |
============================================================
```
- To remove a book you can type `remove book`, and type the id of the book you want to remove when prompted to do so. See the exemple bellow:
```bash
>>> remove book
Type the id of the book: 0

```
- To export a file simply type `export <file_path>`, where the `<file_path>` should be replaced by the path to the file you want to create. Exemple:
```bash
>>> export booklist.rc

```
- To load the file into the program you can use the `import <file_path>`, the books on the file will get added to the current booklist. Exemple:
```bash
>>> import booklist.rc
```
- To list the commands while into the program simply type help:
```bash
>>> help
```
- Type `q` on the prompt to quit.
