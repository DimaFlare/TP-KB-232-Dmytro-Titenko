
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "surname":"Singer", "phone":"0631234567", "email":"ghostbuster123@gmail.com"},
    {"name":"Emma", "surname":"Watson","phone":"0631234567", "email":"emma1990@gmail.com"},
    {"name":"Jon", "surname":"Wick", "phone":"0631234567", "email":"qwerty@gmail.com"},
    {"name":"Zak", "surname":"Snyder", "phone":"0631234567", "email":"zakcool000@ukr.net"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ", surname is " + elem["surname"] + ", Phone is " + elem["phone"] + ", email is " + elem["email"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    surname = input("Pease enter student surname: ")
    phone = input("Please enter student phone: ")
    email = input("Pease enter student email: ")

    newItem = {"name": name, "surname": surname, "phone": phone, "email": email}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")

    position = -1
    for item in list:
        if name == item["name"]:
            position = list.index(item)
            break
    if position == -1:
        print("Element was not found")
    else:
        surname = input("Pease enter new surname: ")
        phone = input("Please enter new phone: ")
        email = input("Pease enter new email: ")

        del list[position]

        newItem = {"name": name, "surname": surname, "phone": phone, "email": email}
        insertPosition = 0
        for item in list:
            if name > item["name"]:
                insertPosition += 1
            else:
                break
        list.insert(insertPosition, newItem)
        print("Info for " + name + " updated!")


def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()