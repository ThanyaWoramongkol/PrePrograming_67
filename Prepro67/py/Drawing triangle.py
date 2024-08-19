"""Drawing +"""

def main(size):
    """-"""
    for col in range(size):
        for row in range(size):
            if col >= row:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
