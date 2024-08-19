"""Leap year"""

def main(years):
    """-"""
    ati = False
    if (not years % 400 or years % 100) and not years % 4:
        ati = True
    print(ati)

main(int(input()))
