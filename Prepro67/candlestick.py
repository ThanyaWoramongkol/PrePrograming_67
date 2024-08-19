"""My candlestick is so beautiful"""

def slider(num):
    """-"""
    num = sum(map(int, str(num)))
    while num > 9:
        num = sum(map(int, str(num)))
    return num

def main(spell):
    """-"""
    num = []
    for i in spell:
        store = slider(ord(i))
        num.append(store)
    rope = slider(sum(num))
    for _ in range(rope):
        print(" *")
    print("---\n| |\n---")
main(list(input()))

