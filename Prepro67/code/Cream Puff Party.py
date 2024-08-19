"""Cream Puff Party"""

def main(energy, current):
    """-"""
    calorie = 334
    eat = 0
    while energy > current:
        current += calorie
        calorie += 5
        eat += 1
    print(eat if eat else "Cream Puff Party")
main(float(input()), float(input()))
