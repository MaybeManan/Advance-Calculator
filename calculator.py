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
                result = logarithm()
                if result == "back":
                    continue

            case "6" | "trigno" | "trignometry" | "trigonometry":
                trignometry()

            case _:
                print("Invalid option.")

        ask = input("\nWould you like to return to the main menu? (yes/no): ").strip().lower()
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
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 0:
            return "back" 
    
        elif choice == 1:
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

        elif choice == 2:
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

        ask = input("\nDo you want to perform another logarithmic operation? (yes/no): ").strip().lower()
        if ask not in ("yes", "y"):
            break


def trignometry():
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

    while True:
        print(
            "\nChoose a trigonometric operation:\n"
            "1. Angle Conversion (Degrees ↔ Radians)\n"
            "2. Trigonometric Functions (sin, cos, tan)\n"
            "3. Inverse Trigonometric Functions (asin, acos, atan)\n"
            "0. Back to main menu\n"
        )
        operator = input("Enter your choice: ").strip().lower()

        if operator in ("1", "conversion", "angle conversion"):
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

            evaluate_simple_expression = re.match(
                r"([a-z]+)\s+([-+*/\d.]+)$", expression
            )
            handle_parentheses = re.match(r"([a-z]+)\(([^()]+)\)$", expression)

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

            evaluate_simple_expression = re.match(
                r"([a-z]+)\s+([-+*/\d.]+)$", expression
            )
            handle_parentheses = re.match(r"([a-z]+)\(([^()]+)\)$", expression)

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

        elif operator == "0":
            return
        
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

        ask = (
            input("\nDo you want to perform another trigonometric operation? (yes/no): ")
            .strip()
            .lower()
        )
        if ask not in ("y", "yes"):
            break


if __name__ == "__main__":
    main()
