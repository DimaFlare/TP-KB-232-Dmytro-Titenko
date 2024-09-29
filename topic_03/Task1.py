from topic_02.exceptions.InvalidOperationException import InvalidOperationException

def closeProgram():
    print("Закриваємось! ☻")
    exit()

def doInput(text):
    inp = input(text).strip().lower()
    if inp == "exit":
        closeProgram()
    return inp
def ask():

    a = float(doInput("Введіть a: "))

    operation = doInput("Введіть операцію: ")

    if operation not in ["+", "-", "*", "/"]:
        raise InvalidOperationException

    b = float(doInput("Введіть b: "))

    return a,operation,b


def calc(a,operation,b):
    match operation:
        case "+": return a+b
        case "-": return a-b
        case "*": return a*b
        case "/": return a/b

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
