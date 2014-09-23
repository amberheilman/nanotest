from testcase import TestCase

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
        returned = validate_input(5)
        self.assertTrue(returned)
