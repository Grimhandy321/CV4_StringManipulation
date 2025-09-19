import re


def nonEmptyStringInput(msg):
    _continue = True
    while _continue:
        _input = input(msg)
        if _input == "":
            print("Invalid input")
        else:
            return _input
    return None


