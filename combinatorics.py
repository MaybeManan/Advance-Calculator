from math import factorial


def fact(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    return factorial(n)


def permutation(n, r):
    return fact(n) // fact(n - r)


def combination(n, r):
    return fact(n) // (fact(r) * fact(n - r))
