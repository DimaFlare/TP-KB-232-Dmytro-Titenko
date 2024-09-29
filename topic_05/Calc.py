from calcmodules.Functions import calc
from calcmodules.Operations import ask
from topic_02.exceptions.InvalidOperationException import InvalidOperationException

def start():
    while True:
        print("\nНапишіть exit щоб завершити програму!")
        try:
            a,operation,b = ask()
            print("Результат:", calc(a, operation, b))
        except ValueError:
            print("a,b повинні бути числом")
        except InvalidOperationException:
            print("Операція повинна бути: + - * або /")
        except ZeroDivisionError:
            print("На нуль ділити не можна! :)")

start()