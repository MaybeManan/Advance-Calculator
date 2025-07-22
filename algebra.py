from sympy import sympify, simplify, expand, factor


def simplifies(expr):

    expression = sympify(expr)
    simplified = simplify(expression)

    # If simplification didn't change it, try factoring
    if simplified == expression:
        return factor(expression)
    return simplified


def expands(expr):
    expression = sympify(expr)
    return expand(expression)


def factorize(expr):
    expression = sympify(expr)
    return factor(expression)


def substitute(expr, value):
    # value is a dict
    expression = sympify(expr)
    return expression.subs(value)
