from sympy import symbols, diff, integrate, sympify


def dif(d, x):
    expression = sympify(d)
    return diff(expression, x)


def integrates(i, x):
    expression = sympify(i)
    return integrate(expression, x)


def auto_detect_var(expression):
    expr = sympify(expression)
    Symbols = expr.free_symbols  # This is a set of Symbol objects
    if len(Symbols) == 1:
        return Symbols.pop()
    elif len(Symbols) == 0:
        raise ValueError("No variable found in expression.")
    else:
        print("Multiple variables found:", Symbols)
        var = input("Enter the variable you want to operate on: ")
        for sym in Symbols:
            if sym.name == var:
                return sym
        raise ValueError(f"Variable '{var}' not found in the expression.")