class Handler:
    def __init__(self, a, operation, b):
        self.a = a
        self.operation = operation
        self.b = b

    def calc(self):
        match self.operation:
            case "+":
                return self.a + self.b
            case "-":
                return self.a - self.b
            case "*":
                return self.a * self.b
            case "/":
                return self.a / self.b

