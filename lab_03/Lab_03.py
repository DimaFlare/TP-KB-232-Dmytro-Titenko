from lab_03.modules.FileHandler import FileHandler
from lab_03.modules.Group import Group

def main():
    group = Group()
    fileHandler = FileHandler(group)
    fileHandler.loadArgs()

    while True:
        choice = input("\nВиберіть дію [ Create створити, Update оновити, Delete видалити, Print вивести, Exit вихід, Save зберегти Load завантажити ] ")
        match choice.lower().strip():
            case "create":
                group.addStudent(*group.askParameters())
            case "update":
                group.updateStudent()
            case "delete":
                group.deleteStudent()
            case "print":
                group.printStudents()
            case "exit":
                break
            case "save":
                fileHandler.saveStudents()
            case "load":
                fileHandler.loadStudents()
            case _:
                print("Неправильна команда!")

main()