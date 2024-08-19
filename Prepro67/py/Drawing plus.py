"""Drawing Plus"""

def main(size):
    """-"""
    for col in range(size):
        for row in range(size):
            if col == size//2 or row == size//2:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
