import math

# Common logarithm (base 10)
def log10(x):
    return math.log10(x)

# Natural logarithm (base e)
def ln(x):
    return math.log(x)

# Logarithm with arbitrary base
def log(x, base):
    return math.log(x, base)

# Antilog (base 10)
def antilog10(x):
    return 10 ** x

# Antilog (base e), inverse of natural log
def antiln(x):
    return math.exp(x)

# Antilog with custom base
def antilog(x, base):
    return base ** x

# Constants
E = math.e
