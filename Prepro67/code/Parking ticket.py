"""Parking ticket"""

def main(hour, minute, bill):
    """-"""
    cost = 20
    if hour == 0 and minute == 0:
        cost = 0
    elif hour >= 2 and minute >= 1:
        cost += 40 * ((hour + 1) - 2)
    elif hour >= 3 and minute == 0:
        cost += 40 * (hour - 2)

    if bill >= 500 and (hour or minute):
        cost = 20

    print(cost)

main(int(input()), int(input()), int(input()))
