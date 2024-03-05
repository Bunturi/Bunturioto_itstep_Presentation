class Book:
    def __init__(self, title, author, publication_year):
        # Initialize a Book object with title, author, and publication year.
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        # Return a string representation of the Book object.
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}"
