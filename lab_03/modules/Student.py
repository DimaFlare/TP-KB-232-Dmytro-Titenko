class Student:

    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Ім'я студента: '{self.name}', прізвище: {self.surname}, телефон: {self.phone}, пошта: {self.email})"