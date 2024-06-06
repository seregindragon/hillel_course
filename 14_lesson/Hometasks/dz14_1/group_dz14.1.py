class MaxStudentsExceeded(Exception):
    """Exception raised when adding more than the allowed number of students in a group."""

    def __init__(self, message="Cannot add more than 10 students to the group"):
        self.message = message
        super().__init__(self.message)


class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, {self.record_book}'


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


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

try:
    for i in range(9):  # Attempt to add 9 more students
        gr.add_student(Student('Female', 20 + i, f'Student{i}', f'Lastname{i}', f'AN14{i}'))
except MaxStudentsExceeded as e:
    print(e)

print(gr)
assert str(gr.find_student('Jobs')) == str(st1)
assert gr.find_student('Jobs2') is None
assert isinstance(gr.find_student('Jobs'), Student) is True

gr.delete_student('Lastname1')
print(gr)  # Only 10 students left (one deleted)

gr.delete_student('Lastname1')  # Attempt to delete non-existent student again
