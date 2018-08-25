def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def main(command: str, num1: int = None, num2: int = None):

        if command == "add":
            print(add(int(num1), int(num2)))
        elif command == "sub":
            print(subtract(int(num1), int(num2)))
        elif command == "mul":
            print(multiply(int(num1), int(num2)))
        elif command == "test":
            test()
        elif command == "exit":
            quit()
        else:
            print("no valid command, try add, sub, or mul")


def test():
    print("starting tests")
    assert add(1, 2) == 3
    assert subtract(5, 4) == 1
    assert multiply(10, 100) == 1000
    print("tests completed successfully")


if __name__ == "__main__":
    while True:
        user_input = input("Enter your command, only 2 numbers dumb ass: ")
        arg_list = user_input.split()
        main(*arg_list)


