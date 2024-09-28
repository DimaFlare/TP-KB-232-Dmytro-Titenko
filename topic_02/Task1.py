import math

def ask():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    return a,b,c

def calcDiscriminant(a,b,c):
    return b*b-4*a*c

# ax^2 + bx + c = 0   (5,4,-9 - answer -1.8 1.0)
def calcEquation(a,b,c):
    discriminant = calcDiscriminant(a,b,c)
    if (discriminant < 0):
            return "Koreniv nema"
    elif (discriminant > 0):
        x1 = (-b - math.sqrt(discriminant)) / (2*a)
        x2 = (-b + math.sqrt(discriminant)) / (2*a)
        return x1,x2
    elif (discriminant == 0):
        return -b/2*a

while True:
    try:
        a,b,c = ask()
        print("Result:", calcEquation(a, b, c))
        break
    except ValueError:
        print("Something went wrong! Please enter integer values")
