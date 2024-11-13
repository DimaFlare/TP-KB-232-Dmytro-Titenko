import csv
from sys import argv
from lab_03.modules.Group import Group

class FileHandler:

    def __init__(self, group:Group):
        self.group = group
        self.fileName = None

    def loadArgs(self):
        if (len(argv) == 2 and argv[1].endswith(".csv")):
            self.fileName = argv[1]
        else:
            print("Можливий тільки 1 аргумент та він бути типа: file.csv")
            exit()

    def loadStudents(self):
        with open(self.fileName) as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.group.addStudent(row["name"], row["surname"],row["phone"], row["email"])

        print("Дані студентів завантажені!")

    def saveStudents(self):
        with open(self.fileName, "w", newline='') as file:
            fieldnames = ["name", "surname", "phone", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in self.group.students:
                writer.writerow({
                    "name": student.name,
                    "surname": student.surname,
                    "phone": student.phone,
                    "email": student.email
                })
            print("Збережено!")