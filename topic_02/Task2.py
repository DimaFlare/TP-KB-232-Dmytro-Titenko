from exceptions.InvalidOperationException import InvalidOperationException
def ask():
    a = float(input("Введіть a: "))

    operation = input("Введіть операцію: ").strip()
    if operation not in ["+", "-", "*", "/"]:
        raise InvalidOperationException

    b = float(input("Введіть b: "))

    return a,operation,b


def calc(a,operation,b):
    if (operation == "+"):
        return a+b
    elif (operation == "-"):
        return a-b
    elif (operation == "*"):
        return a*b
    elif (operation == "/"):
        return a/b

def start():
    while True:
        try:
            a,operation,b = ask()
            print("Результат:", calc(a, operation, b))
            break
        except ValueError:
             print("a,b повинні бути числом")
        except InvalidOperationException:
             print("Операція повинна бути: + - * або /")
        except ZeroDivisionError:
             print("На нуль ділити не можна! :)")
    return

start()