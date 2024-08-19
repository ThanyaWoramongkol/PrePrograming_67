"""The Airplane"""

def main(size):
    """-"""
    count = 0
    for i in range(size):
        print(" ", end="")
        for j in range(size):
            if i >= (size - 1) - j:
                print("*", end="")
                count = count + 1
            else:
                print(" ", end="")
        print()
    print(f"The number of stars use {count}")
main(int(input()))
