"""Arrow UP"""

def main():
    """-"""
    center = 6
    for i in range(5+8):
        for j in range(5+8):
            if j == 4 and i <= center: 
                print("*", end="")
            elif j == 4-i:
                print("*", end="")
            elif j == i+4 and i <= center - 2:
                print("*", end="")
            else:
                print(" ", end="")
        if i >= center:
            break
        print()
main()
