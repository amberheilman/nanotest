from unittest import TestCase

def validate_quantity(data):
    try:
        int(data)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    while True:
        quantity = raw_input("Please input quantity: ")
        try:
            int(quantity)
            break
        except ValueError:
            print("Please input an integer!")


    print(quantity)

    price = raw_input("Please input price: ")
    print(price)

    state = raw_input("Please input state: ")
    print(state)


class ValidateQuantityTest(TestCase):

    def should_return_true_on_valid_input(self):
        returned = quantity(5)
        self.assertTrue(returned)
