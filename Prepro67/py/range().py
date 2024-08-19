"""ForLoop_range()"""

def main():
    """Example parameter of range()"""
    for i in range(5):
        print(i, end=" ")
    print("\n1 parameter | range(stop)")
    for i in range(1, 11):
        print(i, end=" ")
    print("\n2 parameter | range(start, stop)")
    for i in range(1, 12, 3):
        print(i, end=" ")
    print("\n3 parameter | range(start, stop, step)")
main()
