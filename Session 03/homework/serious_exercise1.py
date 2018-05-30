items = ['T-shirt', 'Sweater']
while True:
    n = input("Welcome to our shop, what do you want (C, R, U, D)?")

    if n == "R":
        print("Our items:",end=' ')
        print(*items,sep=', ')

    elif n == "C":
        new_item = input("Enter new item: ")
        items.append(new_item)
        print("Our items:",end=' ')
        print(*items,sep=', ')

    elif n == "U":
        position = int(input("Update position: "))
        items[position-1] = input("New item ?")
        print("Our items:",end=' ')
        print(*items,sep=', ')

    elif n == 'D':
        position = int(input("Delete position: "))
        del items[position-1]
        print("Our items:",end=' ')
        print(*items,sep=', ')