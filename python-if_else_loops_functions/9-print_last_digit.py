def print_last_digit(number):
    number = int(repr(number)[-1])

    print("{}".format(int(number)), end="")
    return number
