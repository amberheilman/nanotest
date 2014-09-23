def validate_quantity(data):
    try:
        quantity = int(data)
        if quantity >= 0:
            return True
        else:
            print("Please input a positive number")
    except ValueError:
        return False


def validate_price(price_input):
    try:
        price = float(price_input)
        return True
    except ValueError:
        print("Please input a price")
        return False


if __name__ == '__main__':
    while True:
        quantity = raw_input("Please input quantity: ")

        if validate_quantity(quantity) is True:
            quanity = int(quanity)
            break
        else:
            print("Please input an integer!")

    print(quantity)

    while True:
        price = raw_input("Please input price: ")

        if validate_price(price) is True:
            price = round(float(price), 2)
            break

    print(price)

    state = raw_input("Please input state: ")
    print(state)
