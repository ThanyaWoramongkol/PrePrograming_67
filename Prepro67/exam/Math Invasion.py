"""Math Invasion"""

def func_f(x):
    """-"""
    return (7 * (x ** 2)) + (3 * x) + 11

def func_g(x, y):
    """-"""
    return (((3 * func_f(x)) ** 0.5) / (4 * y)) - (5 * x * y)

def func_h(x, y, z):
    """-"""
    return ((func_g(func_f(z ** 2) + (x ** y), func_g(x * y, func_f(func_g(y, (z ** 5) ** 0.5))))) \
    / ((2 * x) * ((z * (y ** 2)) ** 0.5) + 91)) + ((7 * x * y) / (13 * z)) + 6

def main(x, y, z):
    """-"""
    print(f"{func_h(x, y, z):.3f}", f"{func_g(x, y):.3f}", f"{func_f(x):.3f}", sep="\n")

main(float(input()), float(input()), float(input()))
