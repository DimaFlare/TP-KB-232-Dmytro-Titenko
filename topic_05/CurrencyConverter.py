import requests

rates = {}

def setCurrencysRate():
    request = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    json = request.json()

    for line in json:
        rates.update({line["cc"]: line["rate"]})

    return

def convert(inp, count):
    return rates[inp] * count

def ask():
    while True:
        inp = input("\nВведіть валюту: ").strip().upper()

        if inp == "EXIT":
            print("Завершую програму")
            exit()

        if inp not in rates:
            print("Такої валюти нема. Доступні валюти: ", rates.keys())
        else:
            break

    while True:
        count = input("Введіть кількість: ").lower()

        if count == "exit":
            print("Завершую програму")
            exit()

        try:
            count = float(count)
            break
        except ValueError:
            print("Кількість повинна бути числом!")

    return inp, count

def start():
    setCurrencysRate()

    while True:
        inp,count = ask()
        print(str(count) + " " + inp + " в гривнях:", convert(inp, count))

    return

start()