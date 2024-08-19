"""Arrow UP (while loop)"""

def main(size):
    center = size + 1
    asize = size * 2 + 3
    i = 0
    while i <= asize:
        line = ""
        j = 0
        while j <= asize:
            if j == size - 1 and i <= center:
                line += "*"
                # print("*", end="")
            elif j == (size - 1) - i:
                line += "*"
                # print("*", end="")
            elif j == i + (size - 1) and i <= center - 2:
                line += "*"
                # print("*", end="")
            else:
                line += " "
                # print(" ", end="")
            j += 1
        if i > center:
            break
        print(line)
        i += 1

main(int(input()))