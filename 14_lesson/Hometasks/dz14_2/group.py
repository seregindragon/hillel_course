from student import Student
from exceptions import MaxStudentsExceeded


class Group:
    def __init__(self, number: str) -> None:
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise MaxStudentsExceeded()
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'
