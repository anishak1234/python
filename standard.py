# 1. Import
# 2. def function
# 3. execption handling
# 4. __init__ main()

import math


class Calculator:

    # 4. __init__ constructor
    def __init__(self, number):
        self.number = number

    # 2. Function
    def square_root(self):
        return math.sqrt(self.number)


def main():
    try:
        num = int(input("Enter a number: "))

        obj = Calculator(num)

        result = obj.square_root()

        print("Square root is:", result)

    # 3. Exception handling
    except ValueError:
        print("Please enter a valid number")


# __main__
if __name__ == "__main__":
    main()