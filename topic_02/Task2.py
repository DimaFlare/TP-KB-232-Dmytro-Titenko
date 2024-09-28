from exceptions.InvalidOperationException import InvalidOperationException
def ask():
    a = float(input("Enter a: "))

    operation = str(input("Enter operation: ").strip())
    if operation not in ["+", "-", "*", "/"]:
        raise InvalidOperationException

    b = float(input("Enter b: "))

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

while True:
    try:
        a,operation,b = ask()
        print("Result:", calc(a, operation, b))
        break
    except ValueError:
        print("Data type error. a,b must be float")
    except InvalidOperationException:
        print("Operation must be: + - * or /")
    except ZeroDivisionError:
        print("You can't divide by 0")

