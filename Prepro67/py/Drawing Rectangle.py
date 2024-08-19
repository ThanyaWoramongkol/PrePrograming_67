"""Drawing Rectangle"""

def main(size):
    """-"""
    for _ in range(size):
        for _ in range(size):
            print("*", end="")
        print()
main(int(input()))
