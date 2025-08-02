import pytest
from basic import add, subtract, multiply, divide, power
from algebra import simplifies, expands, factorize, substitute
from calculus_module import dif, integrates
from combinatorics import fact, permutation, combination
from log import log10, ln, log, antilog10, antiln, antilog
from trigno import sin, cos, tan, asin, acos, atan, deg_to_rad, rad_to_deg

# ----- Basic Arithmetic Tests -----

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 2) == 8

def test_divide():
    assert divide(10, 2) == 5.0

def test_power():
    assert power(2, 3) == 8

# ----- Algebra Tests -----

def test_simplify():
    assert str(simplifies("2*x + 3*x")) == "5*x"

def test_expand():
    assert str(expands("(x+1)**2")) == "x**2 + 2*x + 1"

def test_factor():
    assert str(factorize("x**2 - 1")) == "(x - 1)*(x + 1)"

def test_substitute():
    assert substitute("x**2 + y", {"x": 2, "y": 1}) == 5

# ----- Calculus Tests -----

def test_differentiate():
    assert str(dif("x**2")) == "2*x"

def test_integrate():
    assert str(integrates("x")) == "x**2/2"

# ----- Combinatorics Tests -----

def test_fact():
    assert fact(5) == 120

def test_permutation():
    assert permutation(5, 2) == 20

def test_combination():
    assert combination(5, 2) == 10

# ----- Logarithm Tests -----

def test_log10():
    assert round(log10(100), 4) == 2.0

def test_ln():
    assert round(ln(1), 4) == 0.0

def test_custom_log():
    assert round(log(8, 2), 4) == 3.0

def test_antilog10():
    assert round(antilog10(2), 4) == 100.0

def test_antiln():
    assert round(antiln(0), 4) == 1.0

def test_antilog():
    assert round(antilog(2, 3), 4) == 9.0

# ----- Trigonometry Tests -----

def test_sin():
    assert round(sin(30), 2) == 0.5

def test_cos():
    assert round(cos(60), 2) == 0.5

def test_tan():
    assert round(tan(45), 2) == 1.0

def test_asin():
    assert round(asin(0.5), 2) == 30.0

def test_acos():
    assert round(acos(0.5), 2) == 60.0

def test_atan():
    assert round(atan(1), 2) == 45.0

def test_deg_to_rad():
    assert round(deg_to_rad(180), 2) == 3.14

def test_rad_to_deg():
    assert round(rad_to_deg(3.14), 0) == 180
