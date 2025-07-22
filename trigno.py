import math


def deg_to_rad(degrees):
    return math.radians(degrees)


def rad_to_deg(radians):
    return math.degrees(radians)


def sin(degrees):
    return math.sin(deg_to_rad(degrees))


def cos(degrees):
    return math.cos(deg_to_rad(degrees))


def tan(degrees):
    return math.tan(deg_to_rad(degrees))


def cot(degrees):
    return 1 / tan(degrees)


def sec(degrees):
    return 1 / cos(degrees)


def csc(degrees):
    return 1 / sin(degrees)


# Inverse Functions
def asin(x):
    return math.degrees(math.asin(x))


def acos(x):
    return math.degrees(math.acos(x))


def atan(x):
    return math.degrees(math.atan(x))


def acot(x):
    if x == 0:
        raise ValueError("arccot undefined for x = 0")
    return math.degrees(math.atan(1 / x))


def asec(x):
    if abs(x) < 1:
        raise ValueError("arcsec defined only for |x| ≥ 1")
    return math.degrees(math.acos(1 / x))


def acsc(x):
    if abs(x) < 1:
        raise ValueError("arccosec defined only for |x| ≥ 1")
    return math.degrees(math.asin(1 / x))


# trig_funcs = {
#     "sin": sin,
#     "cos": cos,
#     "tan": tan,
#     "cot": cot,
#     "sec": sec,
#     "csc": csc,
#     "asin": asin,
#     "acos": acos,
#     "atan": atan,
#     "acot": acot,
#     "asec": asec,
#     "acsc": acsc,
# }


# if __name__ == "__main__":
#     angle = 30
#     print(f"sin({angle}) = {sin_deg(angle)}")
#     print(f"cot({angle}) = {cot_deg(angle)}")
