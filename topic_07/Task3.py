class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"

students = [
        Student("John", 20),
        Student("Dean", 19),
        Student("Sam", 23),
        Student("Robert", 16),
        Student("Castiel", 18)
]

print("Не відсортовані:",students)

print("Відсортований за віком:", sorted(students, key=lambda student:student.age, reverse=True))
print("Відсортований за ім'ям в алфавітному порядку:", sorted(students, key=lambda student:student.name))