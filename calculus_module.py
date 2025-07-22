from sympy import symbols, diff, integrate, sympify


def dif(d, x):
    x = symbols(x)
    expression = sympify(d)
    return diff(expression, x)


def integrates(i, x):
    x = symbols(x)
    expression = sympify(i)
    return integrate(expression, x)


# Will use it soon
def auto_detect_var(expr):
    Symbols = expr.free_symbols
    if len(Symbols) == 1:
        return symbols.pop()
    elif len(Symbols) == 0:
        raise ValueError("No variable found in expression.")
    else:
        print("Multiple variables found:", Symbols)
        var = input("Enter the variable you want to operate on: ")
        return symbols(var)
