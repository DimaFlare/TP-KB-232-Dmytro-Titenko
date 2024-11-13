def handleExpression(expression):
    output = []
    stack = []

    priority = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

    number = ""

    for c in expression:
        if c == ' ':
            continue

        if c.isdigit():
            number += c
        else:

            if number != "":
                output.append(int(number))
                number = ""

            if c in priority:
                while len(stack) > 0 and stack[-1] != '(' and priority[stack[-1]] >= priority[c]:
                    output.append(stack.pop())
                stack.append(c)

            elif c == '(':
                stack.append(c)
            elif c == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()


    if number != "":
        output.append(int(number))

    while len(stack) > 0:
        output.append(stack.pop())

    return output

def calculate(output):
    stack = []
    for elem in output:
        if elem not in ["+", "-", "*", "/", "^"]:
            stack.append(elem)
            continue

        second = stack.pop()
        first = stack.pop()

        match (elem):
            case "+":
                stack.append(first + second)
            case "-":
                stack.append(first - second)
            case "*":
                stack.append(first * second)
            case "/":
                stack.append(first / second)
            case "^":
                stack.append(first ** second)

    return stack[0]

def main():
    while True:
        expression = input("Введіть вираз: ")

        output = handleExpression(expression)

        print("Результат:", calculate(output))

main()