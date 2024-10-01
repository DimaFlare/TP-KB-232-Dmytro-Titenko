from calcmodules.Functions import calc
from calcmodules.Operations import ask
from topic_02.exceptions.InvalidOperationException import InvalidOperationException
from topic_05.calcmodules.Log import makeLog

def start():
    while True:
        print("\nНапишіть exit щоб завершити програму!")
        try:
            a,operation,b = ask()
            result = calc(a, operation, b)
            print("Результат:", result)
            makeLog(a,operation,b,result)
        except ValueError:
            print("a,b повинні бути числом")
        except InvalidOperationException:
            print("Операція повинна бути: + - * або /")
        except ZeroDivisionError:
            print("На нуль ділити не можна! :)")

start()