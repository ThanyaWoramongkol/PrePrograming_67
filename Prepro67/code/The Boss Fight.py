"""The Boss Fight"""

def main(party):
    """-"""
    print(party[int(input()) % 3 - 1])

main([input() for _ in range(3)])
