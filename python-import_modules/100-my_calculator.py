#!/usr/bin/python3
if __name__ == "__main__":
    """
         imports all functions from a file and handles basic operations.
    """
    from calculator_1 import add, sub, mul, div
    import sys
    length = len(sys.argv) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operators = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in operators.keys():
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        x = int(sys.argv[1])
        y = int(sys.argv[3])
        z = sys.argv[2]
        print("{} {} {} = {}".format(x, z, y, operators[z](x, y)))
