def start():
    list1 = ["Земля", "Юпітер", "Марс"]
    list2 = ["Сонце", "Меркурій"]
    list1.extend(["Уран"])
    list1.extend(list2)
    print("extend() розшрирює список елементами іншого списку: ", list1)

    list1.append(["Kepler-88","Kepler-55","Kepler-66"])
    print("append() додає до списку щось як один елемент: ", list1)

    list1.insert(0, "Andromeda")
    list1.insert(0, "Andromeda")
    list1.insert(-1, "MilkyWay")
    print("insert(index, object) додає елемент на вказаний індекс: ", list1)

    list1.remove("Andromeda")
    print("remove(val) видаляє перший знайдений такий елемент: ", list1)

    list1.clear()
    print("clear() очищує список: ", list1)

    list1 = ["abc", "abcde", "a", "acbdeGGGG", "Gggggggggggg"]
    list1.sort(key=len, reverse=True)  # сортує за довжиною, найдовше буде першим
    print("sort() сортує за різними ключами: ", list1)

    list1.reverse()
    print("reverse() робить елементи у зворотньому напрямку: ", list1)

    list1 = ["Земля", "Марс", 15, "Сатурн", 25]
    list2 = list1.copy()
    print("copy() копіює список: ", list1, list2)
    return

start()