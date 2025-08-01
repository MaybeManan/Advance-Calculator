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
            "0. Quit Calculator\n"
        )

        operation = input(">> ").strip().lower()

        match operation:
            case "0" | "quit" | "exit":
                print("Goodbye!")
                break
            case "1" | "arithmetic" | "basic":
                result = arithmetic()
                if result == "back":
                    continue

            case "2" | "algebra":
                result = algebra()
                if result == "back":
                    continue

            case "3" | "calculus":
                result = calculus()
                if result == "back":
                    continue

            case "4" | "combinatorics":
                result = pnc()
                if result == "back":
                    continue

            case "5" | "log" | "logarithm":
                result = logarithm()
                if result == "back":
                    continue

            case "6" | "trigno" | "trignometry" | "trigonometry":
                result = trignometry()
                if result == "back":
                    continue

            case _:
                print("Invalid option.")

        # ask = (
        #     input("\nWould you like to return to the main menu? (yes/no): ")
        #     .strip()
        #     .lower()
        # )
        # if ask not in ("y", "yes"):
        #     print("See you next time!")
        #     break


def arithmetic():
    from basic import add, subtract, multiply, divide, power

    while True:
        print(
            "\nChoose an arithmetic operation:\n"
            "1. Addition (+)\n"
            "2. Subtraction (-)\n"
            "3. Multiplication (×)\n"
            "4. Division (÷)\n"
            "5. Power (x^y)\n"
            "6. Square Root (√x)\n"
            "0. Back to main menu\n"
        )

        operator = input(">> ").strip().lower()

        if operator in ("0", "back"):
            return "back"

        elif operator in ("6", "root", "√", "r"):
            try:
                a = float(input("Enter number: "))
                if a >= 0:
                    root = a**0.5
                    print(f"√{a} = {root:.2f}")
                else:
                    print("Cannot determine root of imaginary numbers")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif operator in ("5", "power", "^", "p"):
            try:
                a = float(input("Enter number: "))
                b = float(input("Enter power: "))
                print(f"{a}^{b} = {power(a, b):.2f}")
            except ValueError:
                print("Invalid input. Please enter numbers.")

        elif operator in (
            "1",
            "+",
            "addition",
            "sum",
            "2",
            "-",
            "subtraction",
            "3",
            "*",
            "×",
            "multiplication",
            "4",
            "/",
            "÷",
            "division",
        ):

            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if operator in ("1", "+", "addition", "sum"):
                    print(f"{a} + {b} = {add(a, b)}")
                elif operator in ("2", "-", "subtraction"):
                    print(f"{a} - {b} = {subtract(a, b)}")
                elif operator in ("3", "*", "×", "multiplication"):
                    print(f"{a} × {b} = {multiply(a, b)}")
                elif operator in ("4", "/", "÷", "division"):
                    result = divide(a, b)
                    print(f"{a} ÷ {b} = {result:.2f}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
            except ZeroDivisionError:
                print("Cannot divide by zero.")

        else:
            print("Invalid option. Please try again.")

        ask = (
            input("\nDo you want to perform another arithmetic operation? (yes/no): ")
            .strip()
            .lower()
        )
        if ask not in ("y", "yes"):
            break


def algebra(operator):
    from algebra import simplifies, expands, factorize, substitute

    while True:
        print(
            "\nChoose an algebraic operation:\n"
            "1. Simplify Expression\n"
            "2. Expand Expression\n"
            "3. Factor Expression\n"
            "4. Substitute Values in Expression\n"
            "0. Back to main menu\n"
        )
        operator = input(">> ").strip().lower()

        if operator in ("0", "back"):
            return "back"

        expression = input("\nExpression: ")

        if operator in ("1", "simplify"):
            print(simplifies(expression))

        elif operator in ("2", "expand"):
            print(expands(expression))

        elif operator in ("3", "factorise", "factorize"):
            print(factorize(expression))

        elif operator in ("4", "subsitute"):
            print(substitute(expression))

        else:
            print("Invalid operation.")

        ask = (
            input("\nWould you like to solve another algebraic expression?(yes/no): ")
            .strip()
            .lower()
        )
        if ask not in ("yes", "y"):
            break


def calculus():
    from calculus_module import dif, integrates, auto_detect_var

    while True:
        print(
            "\nChoose a calculus operation:\n"
            "1. Differentiation (Find the derivative)\n"
            "2. Integration (Find the integral)\n"
            "0. Back to main menu\n"
        )

        operator = input(">> ").strip().lower()

        if operator in ("0", "back"):
            return "back"

        elif operator in ("differentiation", "1", "d"):
            d = input("Enter the expression to differentiate: ")
            wrt = auto_detect_var(d)
            print(f"f'({wrt}): {dif(d, wrt)}")

        elif operator in ("integration", "2", "i"):
            i = input("Enter the expression to integrate: ")
            wrt = auto_detect_var(i)
            print(f"∫f({wrt})dx = {integrates(i, wrt)} + C")

        else:
            print("Invalid calculus operation.")

        ask = (
            input("\nContinue with more derivatives or integrals?(yes/no): ")
            .strip()
            .lower()
        )
        if ask not in ("yes", "y"):
            break


def pnc(operator):
    from combinatorics import fact, permutation, combination

    while True:
        print(
            "\nChoose a Combinatorics operation:\n"
            "1. Factorial (n!)\n"
            "2. Permutation (nPr)\n"
            "3. Combination (nCr)\n"
            "0. Back to main menu\n"
        )

        operator = input(">> ").strip().lower()

        if operator in ("0", "back"):
            return "back"

        elif operator in ("factorial", "f", "1"):
            n = int(input("Enter n: "))
            print(f"n! = {fact(n)}")

        elif operator in ("permutation", "p", "2"):
            n = int(input("n = "))
            r = int(input("r = "))
            print(f"nPr = {permutation(n, r)}")

        elif operator in ("combination", "c", "3"):
            n = int(input("n = "))
            r = int(input("r = "))
            print(f"nCr = {combination(n, r)}")

        else:
            print("Invalid operation.")

        ask = input("\nContinue with Combinatorics? (yes/no): ").strip().lower()
        if ask not in ("yes", "y"):
            break


def logarithm():
    from log import log10, ln, log, antilog10, antiln, antilog

    while True:
        print(
            "\nChoose the type of logarithmic function:\n"
            "1. Logarithm Functions — Find log base 10, ln (log base e), or log with custom base\n"
            "2. Antilogarithm Functions - Find values like 10^x, e^x, or any base^x\n"
            "0. Back to main menu\n"
        )

        try:
            choice = input("Enter your choice: ")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice in ("0", "back"):
            return "back"

        elif choice in ("1", "log", "logarithm", "simple"):
            print(
                "\nChoose the logarithmic function:\n"
                "1. log10(x)\n"
                "2. ln(x)\n"
                "3. log(x, base)\n"
            )

            try:
                log_choice = int(input("Enter your choice: "))
                if log_choice == 1:
                    x = float(input("Enter value of x: "))
                    print(f"Result: {log10(x):.4f}")
                elif log_choice == 2:
                    x = float(input("Enter value of x: "))
                    print(f"Result: {ln(x):.4f}")
                elif log_choice == 3:
                    x = float(input("Enter value of x: "))
                    base = float(input("Enter base: "))
                    print(f"Result: {log(x, base):.4f}")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")

        elif choice in ("2", "antilog", "antilogarithm"):
            print(
                "\nChoose the antilogarithm function:\n"
                "1. antilog10(x)\n"
                "2. antiln(x)\n"
                "3. antilog(x, base)\n"
            )

            try:
                anti_choice = int(input("Enter your choice: "))
                if anti_choice == 1:
                    x = float(input("Enter value of x: "))
                    print(f"Result: {antilog10(x):.4f}")
                elif anti_choice == 2:
                    x = float(input("Enter value of x: "))
                    print(f"Result: {antiln(x):.4f}")
                elif anti_choice == 3:
                    x = float(input("Enter value of x: "))
                    base = float(input("Enter base: "))
                    print(f"Result: {antilog(x, base):.4f}")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")

        else:
            print("Invalid option. Try again.")

        ask = (
            input("\nDo you want to perform another logarithmic operation? (yes/no): ")
            .strip()
            .lower()
        )
        if ask not in ("yes", "y"):
            break


def trignometry():
    from re import match
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

    while True:
        print(
            "\nChoose a trigonometric operation:\n"
            "1. Angle Conversion (Degrees ↔ Radians)\n"
            "2. Trigonometric Functions (sin, cos, tan)\n"
            "3. Inverse Trigonometric Functions (asin, acos, atan)\n"
            "0. Back to main menu\n"
        )
        operator = input("Enter your choice: ").strip().lower()

        if operator == "0":
            return "back"

        elif operator in ("1", "conversion", "angle conversion"):
            choice = input(
                "\nConvert:\n1. Degrees to Radians\n2. Radians to Degrees\n>> "
            ).strip()
            if choice == "1":
                deg = float(input("Enter angle in degrees: "))
                print(f"{deg}° = {deg_to_rad(deg):.3f} radians")
            elif choice == "2":
                rad = float(input("Enter angle in radians: "))
                print(f"{rad} radians = {rad_to_deg(rad):.2f}°")
            else:
                print("Invalid conversion option.")

        elif operator in ("2", "functions", "trig", "trigonometric functions"):
            expression = (
                input(
                    "\nEnter Trignometric function and angle (e.g. sin 30 or cos(45 + 15)): "
                )
                .strip()
                .lower()
            )

            evaluate_simple_expression = match(r"([a-z]+)\s+([-+*/\d.]+)$", expression)
            handle_parentheses = match(r"([a-z]+)\(([^()]+)\)$", expression)

            if handle_parentheses:
                func_name, input_expr = handle_parentheses.groups()
            elif evaluate_simple_expression:
                func_name, input_expr = evaluate_simple_expression.groups()
            else:
                print("Invalid format. Use: sin 30  or  sin(30+15)")
                continue

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
                    print("Unsupported trigonometric function.")
                else:
                    result = func(value)
                    print(f"{func_name}({input_expr}) = {result:.3f}")
            except Exception as e:
                print(f"Error: {e}")

        elif operator in ("3", "inverse", "inverse trig", "inverse functions"):
            expression = (
                input(
                    "\nEnter Inverse Trignometric function and value (e.g. asin 0.5 or asec(2)): "
                )
                .strip()
                .lower()
            )

            evaluate_simple_expression = match(r"([a-z]+)\s+([-+*/\d.]+)$", expression)
            handle_parentheses = match(r"([a-z]+)\(([^()]+)\)$", expression)

            if handle_parentheses:
                func_name, input_expr = handle_parentheses.groups()
            elif evaluate_simple_expression:
                func_name, input_expr = evaluate_simple_expression.groups()
            else:
                print("Invalid format. Use: asin 0.5  or  acos(0.5)")
                continue

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
                    print("Unsupported inverse function.")
                else:
                    result = func(value)
                    print(f"{func_name}({input_expr}) = {result:.2f}°")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid option.")

        ask = (
            input(
                "\nDo you want to perform another trigonometric operation? (yes/no): "
            )
            .strip()
            .lower()
        )
        if ask not in ("y", "yes"):
            break


if __name__ == "__main__":
    main()
