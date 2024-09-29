import math

def ask():
    a = int(input("Введіть a: "))
    b = int(input("Введіть b: "))
    c = int(input("Введіть c: "))
    return a,b,c

def calcDiscriminant(a,b,c):
    return b*b-4*a*c

# ax^2 + bx + c = 0   (5,4,-9 - answer -1.8 1.0)
def calcEquation(a,b,c):
    discriminant = calcDiscriminant(a,b,c)
    if (discriminant < 0):
            return "Коренів нема :("
    elif (discriminant > 0):
        x1 = (-b - math.sqrt(discriminant)) / (2*a)
        x2 = (-b + math.sqrt(discriminant)) / (2*a)
        return x1,x2
    elif (discriminant == 0):
        return -b/2*a

def start():
    while True:
        try:
            a,b,c = ask()
            print("Результат:", calcEquation(a, b, c))
            break
        except ValueError:
            print("Прошу вводити тільки цілі числа!")
    return
start()
