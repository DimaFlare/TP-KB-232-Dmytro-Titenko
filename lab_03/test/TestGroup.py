import unittest
from unittest.mock import patch

from lab_03.modules.Group import Group

class TestGroup(unittest.TestCase):

    def setUp(self):
        self.group = Group()

    @patch('builtins.input', side_effect=["Test", "Testovich", "123456789", "test@test.com"])
    def test_addStudent(self, mock_input):
        name, surname, phone, email = self.group.askParameters()

        self.group.addStudent(name, surname, phone, email)

        assert len(self.group.students) == 1
        assert self.group.students[0].name == "Test"
        assert self.group.students[0].surname == "Testovich"

    @patch('builtins.input', side_effect=["Test", "TestNewName", "NewSurname", "987654321", "new@new.com"])
    def test_updateStudent(self, mock_input):
        self.test_addStudent()
        self.group.updateStudent()

        assert self.group.students[0].name == "TestNewName"
        assert self.group.students[0].surname == "NewSurname"
        assert self.group.students[0].phone == "987654321"
        assert self.group.students[0].email == "new@new.com"


    @patch('builtins.input', side_effect=["Test"])
    def test_deleteStudent(self, mock_input):
        self.test_addStudent()
        self.group.deleteStudent()

        assert len(self.group.students) == 0

