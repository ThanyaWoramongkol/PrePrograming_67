"""Sort number please"""

def main(number: list, position: str):
    """-"""
    if position == "low to high":
        number.sort()
    else:
        number.sort(reverse=True)
    print(*number)
main([int(i) for i in input().split()], input())
