class User():

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __str__(self): # Строкове уявлення об'єкту неформального плану, може містити будь яку зручну для розуміння інформацію
        return f"Користувач з логіном {self.login} та паролем {self.password}"

    def __repr__(self): # Строкове уявлення об'єкту формального плану, зазвичай повинен бути таким, щоб з цього можно було створити об'єкт
        return f"User(login='{self.login}', password={self.password})"

Ivan = User("ivanqwerty", "12345")

print(Ivan)
print(repr(Ivan))