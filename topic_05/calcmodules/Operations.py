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