import json
from faker import Faker
import os

fake = Faker()


class Book:
    def __init__(self, title, author, publication_year):
        # Initialize a Book object with title, author, and publication year.
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        # Return a string representation of the Book object.
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}"


class BookManager:
    def __init__(self):
        # Initialize a BookManager object.
        self.books = []

    @staticmethod
    def is_json_file_empty(filename):
        # Check if the JSON file is empty.
        return not os.path.exists(filename) or os.path.getsize(filename) == 0

    @staticmethod
    def custom_encoder(obj):
        # Custom JSON encoder for Book objects.
        if isinstance(obj, Book):
            return {
                "title": obj.title,
                "author": obj.author,
                "publication_year": obj.publication_year,
            }
        return obj

    @staticmethod
    def custom_decoder(json_data):
        # Custom JSON decoder for Book objects.
        return Book(json_data['title'], json_data['author'], json_data['publication_year'])

    @staticmethod
    def write_data(lst):
        # Write data to a JSON file.
        with open("book_data.json", "w") as json_file:
            json.dump(lst, json_file, default=BookManager.custom_encoder, indent=4)

    @staticmethod
    def read_data():
        # Read data from a JSON file.
        with open("book_data.json", "r") as read_json:
            python_data = json.load(read_json, object_hook=BookManager.custom_decoder)
            return python_data

    def generate_fake_books(self, num_books):
        # Generate fake books using Faker and write them to the JSON file.
        self.books = []
        for _ in range(num_books):
            title = fake.catch_phrase()
            author = fake.name()
            publication_year = fake.year()
            self.books.append(Book(title, author, publication_year))
        self.write_data(self.books)


def main():
    # Main function to run the program.
    manager = BookManager()

    if manager.is_json_file_empty("book_data.json"):
        manager.generate_fake_books(10)

    while True:
        print("\nMenu:")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Search Book by Title")
        print("4. Exit")

        choice = input("Enter your choice: ")