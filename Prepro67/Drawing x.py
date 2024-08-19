"""-"""

def main(height):
    """-"""
    for i in range(height):
        for j in range(height):
            if i == j:
                print("*", end=' ')
            elif i+j == height-1:
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()
main(int(input()))