import json


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

    # Custom JSON encoder for Student object
    @staticmethod
    def custom_encoder(obj):
        if isinstance(obj, Student):
            return {
                "name": obj.name,
                "roll_number": obj.roll_number,
                "grade": obj.grade
            }
        return obj

    # Custom JSON decoder for Student object
    @staticmethod
    def custom_decoder(json_data):
        return Student(json_data['name'], json_data['roll_number'], json_data['grade'])

    # Write data to JSON file
    @staticmethod
    def write_data(lst):
        with open("student_data.json", "w") as json_file:
            json.dump(lst, json_file, default=StudentManagement.custom_encoder, indent=4)

    # Read data from JSON file
    @staticmethod
    def read_data():
        with open("student_data.json", "r") as read_json:
            python_data = json.load(read_json, object_hook=StudentManagement.custom_decoder)
            return python_data

    # Bubble sort by roll number
    def bubble_sort(self):
        n = len(self.students)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.students[j].roll_number > self.students[j + 1].roll_number:
                    self.students[j], self.students[j + 1] = self.students[j + 1], self.students[j]
        return self.students

    # Binary search by roll number
    def binary_search(self, roll_number):
        low = 0
        high = len(self.students) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.students[mid].roll_number == roll_number:
                return self.students[mid]
            elif self.students[mid].roll_number < roll_number:
                low = mid + 1
            else:
                high = mid - 1
        return None




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