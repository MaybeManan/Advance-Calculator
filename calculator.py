# Error handling not done
# Break whole logic in different functions not only main()
# Add a Menu option

from basic import add, subtract, multiply, divide, power
from calculus_module import dif, integrates
from combinatorics import fact, permutation, combination
from algebra import simplifies, expands, factorize, substitute
from log import log10, ln, log, antilog10, antiln, antilog
from trigno import (
    deg_to_rad,
    rad_to_deg,
    sin,
    cos,
    tan,
    cot,
    sec,
    csc,
    asin,
    acos,
    atan,
    acot,
    asec,
    acsc,
)


def main():
    while True:
        print(
            "Choose a category:\n"
            "1. Arithmetic (Basic Math: +, −, ×, ÷, powers, roots)\n"
            "2. Algebra and Exponents\n"
            "3. Calculus (Differentiation and Integration)\n"
            "4. Combinatorics (Factorial, nPr, nCr)\n"
            "5. Logarithm (log, ln, custom base, antilog)\n"
            "6. Trigonometry (Conversion, Trig functions, Inverse functions)\n"
        )

        operation = input("> ").strip().lower()
        if operation in ("arithmetic", "1"):
            print(
                "\nChoose an arithmetic operation:\n"
                "1. Addition (+)\n2. Subtraction (−)\n3. Multiplication (×)\n"
                "4. Division (÷)\n5. Power (x^y)\n6. Root (√x)\n"
            )

            operator = input("> ").strip().lower()
            print(arithmetic(operator))

        elif operation in ("algebra", "2"):
            print(
                "\nChoose an algebraic operation:\n"
                "1. Simplify Expression\n"
                "2. Expand Expression\n"
                "3. Factor Expression\n"
                "4. Substitute Values in Expression\n"
            )
            operator = input("> ").strip().lower()
            print(algebra(operator))

        elif operation in ("calculus", "3"):
            print(
                "\nChoose a calculus operation:\n1. Differentiation (Find the derivative)\n2. Integration (Find the integral)\n"
            )
            operator = input("> ").strip().lower()
            print(calculus(operator))

        elif operation in ("combinatorics", "4"):
            print(
                "\nChoose a combinatorics operation:\n1. Factorial (n!)\n2. Permutation (nPr)\n3. Combination (nCr)\n"
            )
            operator = input("> ").strip().lower()
            print(pnc(operator))

        elif operation in ("log", "logarithm", "5"):
            print(
                "\nSelect a logarithmic operation:\n1. Log Functions — log base 10, ln (log base e), or log with custom base\n"
                "2. Antilog Functions — Find values like 10^x, e^x, or any base^x\n"
            )
            operator = input("> ").strip().lower()
            print(logarithm(operator))

        elif operation in ("trigno", "trignometry", "6"):
            print(
                "\nChoose a trigonometric operation:\n1. Angle Conversion (Degrees ↔ Radians)\n"
                "2. Trigonometric Functions (sin, cos, tan)\n"
                "3. Inverse Trigonometric Functions (asin, acos, atan)\n"
            )
            operator = input("> ").strip().lower()
            print(trignometry(operator))

        else:
            print("Invalid operator.")

        ask = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if ask not in ("y", "yes"):
            print("Goodbye!")
            break


def arithmetic(operator):
    if operator in ("root", "√", "r", "6"):
        a = int(input("Number: "))
        if a >= 0:
            root = a**0.5
            return f"{root:.2f}"
        else:
            return "Cannot determine root of imaginary numbers"

    elif operator in ("power", "^", "p", "5"):
        a = float(input("Number: "))
        b = float(input("Power: "))
        return f"{power(a, b):.2f}"

    a = int(input("First number: "))
    b = int(input("Second number: "))
    if operator in ("addition", "+", "sum", "1"):
        return add(a, b)
    elif operator in ("subtraction", "-", "2"):
        return subtract(a, b)
    elif operator in ("multiplication", "*", "×", "3"):
        return multiply(a, b)
    elif operator in ("division", "/", "÷", "4"):
        return f"{divide(a, b):.2f}"
    else:
        return "Invalid operation."


def algebra(operator): ...


def calculus(operator):
    if operator in ("differentiation", "1", "d"):
        d = input("Enter the expression to differentiate: ")
        wrt = input("With respect to: ")
        return dif(d, wrt)
    elif operator in ("integration", "2", "i"):
        i = input("Enter the expression to integrate: ")
        wrt = input("With respect to: ")
        return integrates(i, wrt)
    else:
        return "Invalid calculus operation."


def pnc(operator):
    if operator in ("factorial", "f", "1"):
        n = int(input("Enter n: "))
        return f"n! = {fact(n)}"
    elif operator in ("permutation", "p", "2"):
        n = int(input("n = "))
        r = int(input("r = "))
        return f"nPr = {permutation(n, r)}"
    elif operator in ("combination", "c", "3"):
        n = int(input("n = "))
        r = int(input("r = "))
        return f"nCr = {combination(n, r)}"
    else:
        return "Invalid combinatorics operation."


def trignometry(operator): ...


def logarithm(operator): ...


if __name__ == "__main__":
    main()
