

class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"


class StudentManagement:
    def __init__(self):
        self.students = []


def main():
    management = StudentManagement()

    while True:
        print("\nMenu:")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Student Grade")
        print("5. Exit")

        choice = input("Enter your choice: ")


if __name__ == '__main__':
    main()