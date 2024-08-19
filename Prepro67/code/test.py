"""Arrow UP"""

def main(size):
    """-"""
    center = size + 1
    asize = size * 2 + 3
    for i in range(asize):
        for j in range(asize):
            if j == size - 1 and i <= center: 
                print("*", end="")
            elif j == (size - 1) - i:
                print("*", end="")
            elif j == i + (size - 1) and i <= center - 2:
                print("*", end="")
            else:
                print(" ", end="")
        if i >= center:
            break
        print()
main(int(input()))


# number = 5
# star = "*"
# loop
#     print(star)
#     star += "*"
