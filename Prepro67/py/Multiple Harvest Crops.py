"""Stardew"""

def main(name, growtime, regrowth, price, amount, date):
    """-"""
    income = 0
    count = 0
    harvest = ""
    date += growtime

    if date <= 28:
        while date <= 28:
            harvest += str(date) + " "
            date += regrowth
            income += price * amount
            count += 1
        print(f"The {name} will be harvestable for {count} days in this Season")
        print(f"Harvestable days: {harvest}")
    else:
        print(f"The Season will end before you can harvest your {name}")
    print(f"Youe income will be {income:,} G")
main(input(), int(input()), int(input()), int(input()), int(input()), int(input()))
