def ask():
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    return a,b,c

def calcDiscriminant(a,b,c):
    return b*b-4*a*c

a,b,c, = ask()
print("Результат: ", calcDiscriminant(a,b,c))
