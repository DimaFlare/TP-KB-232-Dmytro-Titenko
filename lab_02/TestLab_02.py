from lab_02.Lab_02 import students, addNewElement, deleteElement

def test_addNewElement():
    addNewElement("Test", "Testovich", "123456789", "test@test.ua")
    assert len(students) == 1
    assert students[0]["name"] == "Test"

def test_updateElement():
    print(students)
    name = "Test"

    position = -1
    for item in students:
        if name == item["name"]:
            position = students.index(item)
            break
    assert position != 1

    surname = "NewSurname"
    phone = students[position]["phone"]
    email = students[position]["email"]

    assert name is not None
    assert surname is not None
    assert phone is not None
    assert email is not None

    del students[position]

    addNewElement(name, surname, phone, email)

    assert students[position]["surname"] == "NewSurname"

    print("Info for updated!")

def test_deleteElement():
    deleteElement("Test")
    assert len(students) == 0
