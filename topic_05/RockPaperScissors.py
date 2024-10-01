import random

choices = ("rock", "paper", "scissors")

beat = {
        "rock":"scissors",
        "scissors":"paper",
        "paper":"rock"
        }

def ask():
    while True:
        choice = input("\nОберіть хід: ").strip().lower()
        if choice == "exit":
            print("Завершую гру")
            exit()

        if choice in choices:
            break
        else:
            print("Хід повинен бути одним із:", choices)
            continue

    return choice


def play(choice):
    randomChoice = choices[random.randint(0, len(choices)-1)]
    if choice == randomChoice:
        return "Нічия. Суперник вибрав: " + randomChoice
    elif randomChoice == beat[choice]:
        return "Ви виграли. Суперник вибрав: " + randomChoice
    else:
        return "Ви програли. Суперник вибрав: " + randomChoice

    return
def start():
    while True:
        print(play(ask()))
    return

start()