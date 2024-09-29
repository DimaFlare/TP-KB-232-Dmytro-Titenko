def insert(list, a):
    if not list:
        list.extend([a])
    else:
        for e in list:
            if a >= list[len(list)-1]:
                list.insert(len(list), a)
                break
            elif a <= e:
                list.insert(list.index(e), a)
                break
    return

def start():
    list = []
    print("Список:", list)

    while True:
        try:
            a = int(input("Введіть а: "))
        except ValueError:
            print("a повинно бути цілим числом")
            continue

        insert(list,a)
        print("Список:",list)

    return

start()