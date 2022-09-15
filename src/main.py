import sys
from math import *


USAGE = """Usage: math [--debug|-d] EXPRESSION"""
DEBUG = False


def main() -> None:
    arguments = sys.argv[1:]
    global DEBUG
    if len(arguments) == 0:
        print(USAGE)
        sys.exit(1)
    if arguments[0] in ["--debug", "-d"]:
        DEBUG = True
        print("Debug mode on")
        print("Passed arguments: ", arguments)
        arguments.pop(0)
    if len(arguments) != 1:
        print(USAGE)
        sys.exit(1)
    expression = arguments[0]
    if DEBUG:
        print(f"Expression: {expression}")
    result = eval(expression)
    if DEBUG:
        print(f"Result: {result}")
    else:
        print(result)


if __name__ == "__main__":
    main()
