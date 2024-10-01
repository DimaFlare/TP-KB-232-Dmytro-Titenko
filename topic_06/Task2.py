journal = [
    {"name": "Serhiy", "score": 10},
    {"name": "Oleg", "score": 3},
    {"name": "Katerine", "score": 7},
    {"name": "Vitaliy", "score": 8},
    {"name": "Emma", "score": 4},
]

print("Не відсортований:", journal)

print("Відсортований за найвищим балом:", sorted(journal, key=lambda x: x['score'], reverse=True))
print("Відсортований за ім'ям в алфавітному порядку:", sorted(journal, key=lambda x: x['name']))