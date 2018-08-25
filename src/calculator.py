def subtract(nums):
    if len(nums) > 0:
        return nums[0] - sum(nums[1:])
    return


def multiply(nums):
    result = 1
    for x in nums:
        result = result * x
    return result

#
# List comprehensions:
# l2 and ls will be equal...
#
# l = [1,2,3]
#
# l2 = [elem*2 for elem in l]
#
#
# ls = []
# for elem in l:
#     ls.append(elem*2)


def calculator(command: str, *nums):
    if command == "add":
        nums_int = [int(elem) for elem in nums]
        res = sum(nums_int)
        return res
    elif command == "sub":
        nums_int = [int(elem) for elem in nums]
        res = subtract(nums_int)
        return res
    elif command == "mul":
        nums_int = [int(elem) for elem in nums]
        res = multiply(nums_int)
        return res
    elif command == "test":
        test()
        return "Tests completed successfully!"
    elif command == "exit":
        print("Bye!")
        quit()
    else:
        return "no valid command, try add, sub, or mul"

def main():
    print("HALLSTEINS CALCULATOR")
    print("---------------------")
    while True:
        user_input = input("Command: ")
        arg_list = user_input.split()
        output = calculator(*arg_list)
        print(output)


def test():
    assert calculator("add", 1, 2, 3, 4) == 10
    assert calculator("sub", 1, 2, 3, 4) == -8
    assert calculator("mul", 10, 100, 1000, 10000) == 10000000000


if __name__ == "__main__":
    main()


