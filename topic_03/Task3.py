def start():
    dictionary1 = {
        "key1": "Value1",
        "key2": "Value2",
        "key3": "Value3"
    }
    dictionary2 = {
        "key4": "Value4",
        "key5": "Value5",
        "key6": "Value6"
    }

    dictionary1.update(dictionary2)
    print("update() об'єднує два словника: ", dictionary1)

    del dictionary1["key5"]
    print("del видаляє елемент за ключем: ", dictionary1)

    print("keys() виводить ключі: ", dictionary1.keys())
    print("values() виводить значення: ", dictionary1.values())
    print("items() виводить ключі і їх значення: ", dictionary1.items())

    dictionary1.clear()
    print("clear() очищує словник: ", dictionary1)

    return

start()