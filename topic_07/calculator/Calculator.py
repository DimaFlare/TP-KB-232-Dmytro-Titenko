from topic_02.exceptions.InvalidOperationException import InvalidOperationException
from topic_07.calculator.Handler import Handler
from topic_07.calculator.Interact import Interact

class Calculator:

    def start(self):
        while True:
            print("\nНапишіть exit щоб завершити програму!")
            try:
                interact = Interact()
                a, operation, b = interact.ask()

                handler = Handler(a,operation,b)
                print("Результат:", handler.calc())

            except ValueError:
                print("a,b повинні бути числом")
            except InvalidOperationException:
                print("Операція повинна бути: + - * або /")
            except ZeroDivisionError:
                print("На нуль ділити не можна! :)")
