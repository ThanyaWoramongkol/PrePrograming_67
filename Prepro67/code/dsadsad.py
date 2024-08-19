"""+"""

def func_f(x):
    fx = 3 * x + 5
    return fx

def func_g(x):
    gx = (func_f(4 * x) + 23) / 2
    return gx

def func_h(x, y):
    A = func_f(3 * y) + (2 * x)
    B = 2 * y
    C = 4 * y
    hxy = (func_g(A) - func_g(B)) * (func_f(C) + (5 * x))
    return hxy

def main():
    """-"""
    global x, y
    x, y = float(input()), float(input())
    z = func_h(x, y)
    print(f"{z:.2f}")

main()
