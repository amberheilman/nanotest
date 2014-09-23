def validate_quantity(data):
    try:
        int(data)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    while True:
        quantity = raw_input("Please input quantity: ")

        if validate_quantity(quantity) == True:
            break
        else:
            print("Please input an integer!")

    print(quantity)

    price = raw_input("Please input price: ")
    print(price)

    state = raw_input("Please input state: ")
    print(state)
