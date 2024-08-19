"""My candlestick is so beautiful"""

def main(spell):
    """-"""
    num = []
    for i in spell:
        store = sum([int(j) for j in str(ord(i))]) ## rope = sum(map(int, str(ord(i)))))
        if store > 9:
            store = sum([int(j) for j in store])
        num.append(store)
    rope = sum([int(lek) for lek in str(sum(num))]) ## rope = sum(map(int, str(sum(num))))
    while rope > 9:
        rope = sum([int(j) for j in str(rope)]) ## rope = sum(map(int, str(rope)))
    for _ in range(rope):
        print(" *")
    print("---\n| |\n---")
main(list(input()))
