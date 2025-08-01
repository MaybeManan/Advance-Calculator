# Error handling not done
# Add a Menu option


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

        operation = input(">> ").strip().lower()

        match operation:
            case "1" | "arithmetic":
                print(
                    "\nChoose an arithmetic operation:\n"
                    "1. Addition (+)\n2. Subtraction (−)\n3. Multiplication (×)\n"
                    "4. Division (÷)\n5. Power (x^y)\n6. Root (√x)\n"
                )
                operator = input(">> ").strip().lower()
                print(arithmetic(operator))

            case "2" | "algebra":
                print(
                    "\nChoose an algebraic operation:\n"
                    "1. Simplify Expression\n"
                    "2. Expand Expression\n"
                    "3. Factor Expression\n"
                    "4. Substitute Values in Expression\n"
                )
                operator = input(">> ").strip().lower()
                print(algebra(operator))

            case "3" | "calculus":
                print(
                    "\nChoose a calculus operation:\n"
                    "1. Differentiation (Find the derivative)\n"
                    "2. Integration (Find the integral)\n"
                )
                operator = input(">> ").strip().lower()
                print(calculus(operator))

            case "4" | "combinatorics":
                print(
                    "\nChoose a combinatorics operation:\n"
                    "1. Factorial (n!)\n"
                    "2. Permutation (nPr)\n"
                    "3. Combination (nCr)\n"
                )
                operator = input(">> ").strip().lower()
                print(pnc(operator))

            case "5" | "log" | "logarithm":
                print(
                    "\nSelect a logarithmic operation:\n"
                    "1. Log Functions — log base 10, ln (log base e), or log with custom base\n"
                    "2. Antilog Functions — Find values like 10^x, e^x, or any base^x\n"
                )
                operator = input(">> ").strip().lower()
                print(logarithm(operator))

            case "6" | "trigno" | "trignometry" | "trigonometry":
                print(
                    "\nChoose a trigonometric operation:\n"
                    "1. Angle Conversion (Degrees ↔ Radians)\n"
                    "2. Trigonometric Functions (sin, cos, tan)\n"
                    "3. Inverse Trigonometric Functions (asin, acos, atan)\n"
                )
                operator = input(">> ").strip().lower()
                print(trignometry(operator))

            case _:
                print("Invalid option.")

        ask = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if ask not in ("y", "yes"):
            print("Goodbye!")
            break


def arithmetic(operator):
    from basic import add, subtract, multiply, divide, power

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


def algebra(operator):
    from algebra import simplifies, expands, factorize, substitute

    expression = input("Expression: ")
    if operator in ("1", "simplify"):
        return simplifies(expression)
    elif operator in ("2", "expand"):
        return expands(expression)
    elif operator in ("3", "factorise", "factorize"):
        return factorize(expression)
    elif operator in ("4", "subsitute"):
        return substitute(expression)
    else:
        return "Invalid operation."


def calculus(operator):
    from calculus_module import dif, integrates

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
    from combinatorics import fact, permutation, combination

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


def logarithm(operator):
    from log import log10, ln, log, antilog10, antiln, antilog


def trignometry(operator):
    import re
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

    if operator in ("1", "conversion", "angle conversion"):
        choice = input(
            "Convert:\n1. Degrees to Radians\n2. Radians to Degrees\n>> "
        ).strip()
        if choice == "1":
            deg = float(input("Enter angle in degrees: "))
            return f"{deg}° = {deg_to_rad(deg):.3f} radians"
        elif choice == "2":
            rad = float(input("Enter angle in radians: "))
            return f"{rad} radians = {rad_to_deg(rad):.2f}°"
        else:
            return "Invalid conversion option."

    elif operator in ("2", "functions", "trig", "trigonometric functions"):
        expression = (
            input("Enter trig function and angle (e.g. sin 30 or cos(45 + 15)): ")
            .strip()
            .lower()
        )

        evaluate_simple_expression = re.match(r"([a-z]+)\s+([-+*/\d.]+)$", expression)
        handle_parentheses = re.match(r"([a-z]+)\(([^()]+)\)$", expression)

        if handle_parentheses:
            func_name, input_expr = handle_parentheses.groups()
        elif evaluate_simple_expression:
            func_name, input_expr = evaluate_simple_expression.groups()
        else:
            return "Invalid format. Use: sin 30  or  sin(30+15)"

        try:
            value = eval(input_expr, {"__builtins__": {}}, {})
            func_map = {
                "sin": sin,
                "cos": cos,
                "tan": tan,
                "cot": cot,
                "sec": sec,
                "csc": csc,
            }
            func = func_map.get(func_name)
            if func is None:
                return "Unsupported trigonometric function."
            result = func(value)
            return f"{func_name}({input_expr}) = {result:.3f}"
        except Exception as e:
            return f"Error: {e}"

    elif operator in ("3", "inverse", "inverse trig", "inverse functions"):
        expression = (
            input("Enter inverse trig function and value (e.g. asin 0.5 or asec(2)): ")
            .strip()
            .lower()
        )

        evaluate_simple_expression = re.match(r"([a-z]+)\s+([-+*/\d.]+)$", expression)
        handle_parentheses = re.match(r"([a-z]+)\(([^()]+)\)$", expression)

        if handle_parentheses:
            func_name, input_expr = handle_parentheses.groups()
        elif evaluate_simple_expression:
            func_name, input_expr = evaluate_simple_expression.groups()
        else:
            return "Invalid format. Use: asin 0.5  or  acos(0.5)"

        try:
            value = eval(input_expr, {"__builtins__": {}}, {})
            inverse_map = {
                "asin": asin,
                "acos": acos,
                "atan": atan,
                "acot": acot,
                "asec": asec,
                "acsc": acsc,
            }
            func = inverse_map.get(func_name)
            if func is None:
                return "Unsupported inverse function."
            result = func(value)
            return f"{func_name}({input_expr}) = {result:.2f}°"
        except Exception as e:
            return f"Error: {e}"

    else:
        return "Invalid trigonometric operation."


if __name__ == "__main__":
    main()
