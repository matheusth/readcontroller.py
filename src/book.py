class Book:
    def __init__(self, *vargs) -> None:
        self.name = vargs[0]
        self.author = vargs[1]
        self.edition = vargs[2]
        self.currentChapter = vargs[3]
