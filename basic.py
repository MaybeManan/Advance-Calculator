import sys


def main():
    a = int(input("First number: "))
    b = int(input("Second number: "))
    operation = (
        input("Choose initials or Symbol of the Operation: Addition(+), Subtraction(-), Multiplication(*), Division(/)\n")
        .strip()
        .lower()
    )

    if operation in ("addition", "+", "a"):
        print(add(a, b))
    if operation in ("subtraction", "-", "s"):
        print(subtract(a, b))
    if operation in ("multiplication", "*", "m"):
        print(multiply(a, b))
    if operation in ("division", "/", "d"):
        print(f"{divide(a, b):.2f}")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # ZeroDivisionError needs to be here instead of if else
    if b == 0:
        print("Denominator cannot be 0")
        main()
    else:
        return a / b
    

def power(a, p):
    return a ** p


if __name__ == "__main__":
    main()