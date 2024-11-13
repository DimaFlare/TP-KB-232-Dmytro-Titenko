from lab_03.modules.Student import Student

class Group:

    def __init__(self):
        self.students = []

    def printStudents(self):
        if (len(self.students) == 0):
            print("Список пустий, завантажте його командою load")
        else:
            print(" ")
            for elem in self.students:
                print(elem)

    def askParameters(self):
        name = input("Введіть ім'я: ")
        surname = input("Введіть прізвище: ")
        phone = input("Введіть номер телефону: ")
        email = input("Введіть електронну пошту: ")
        return name, surname, phone, email

    def addStudent(self, name, surname, phone, email):
        student = Student(name, surname, phone, email)

        insertPosition = 0
        for item in self.students:
            if name > item.name:
                insertPosition += 1
            else:
                break

        self.students.insert(insertPosition, student)
        print("Новий студент був доданий")
        return

    def deleteStudent(self):
        name = input("Введіть ім'я студента на видалення: ")
        deletePosition = -1
        for item in self.students:
            if name == item.name:
                deletePosition = self.students.index(item)
                break
        if deletePosition == -1:
            print("Студента не знайдено")
        else:
            print("Видаляю позицію " + str(deletePosition))
            del self.students[deletePosition]
            print("Студент був видалений")
        return

    def updateStudent(self):
        name = input("Введіть ім'я студента інформацію якого ви хочете змінити: ")

        position = -1
        for item in self.students:
            if name == item.name:
                position = self.students.index(item)
                break
        if position == -1:
            print("Студента не знайдено")
        else:

            student = self.students[position]

            name = input("Введіть нове ім'я. Натисніть ентер якщо не бажаєте це змінювати: ")
            if not name:
                name = student.name

            surname = input("Введіть нове прізвище. Натисніть ентер якщо не бажаєте це змінювати:  ")
            if not surname:
                surname = student.surname

            phone = input("Введіть новий номер телефону. Натисніть ентер якщо не бажаєте це змінювати: ")
            if not phone:
                phone = student.phone

            email = input("Введіть нову електронну пошту. Натисніть ентер якщо не бажаєте це змінювати: ")
            if not email:
                email = student.email

            del self.students[position]

            self.addStudent(name, surname, phone, email)

            print("Інформація про студента оновлена")