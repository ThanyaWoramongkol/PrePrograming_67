"""Secret Message"""

def main(count):
    """1 star"""
    output = ''
    for i in range(count):
        txt = input()
        if i > len(txt)-1:
            output += txt[len(txt)-1]
            continue
        output += txt[i]
    print(output)
main(int(input()))
