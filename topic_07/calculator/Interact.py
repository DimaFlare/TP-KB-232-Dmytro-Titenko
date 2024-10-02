from topic_02.exceptions.InvalidOperationException import InvalidOperationException

class Interact:

    def closeProgram(self):
        print("Закриваємось! ☻")
        exit()

    def doInput(self, text):
        inp = input(text).strip().lower()
        if inp == "exit":
            self.closeProgram()
        return inp

    def ask(self):

        a = float(self.doInput("Введіть a: "))

        operation = self.doInput("Введіть операцію: ")

        if operation not in ["+", "-", "*", "/"]:
            raise InvalidOperationException

        b = float(self.doInput("Введіть b: "))

        return a, operation, b