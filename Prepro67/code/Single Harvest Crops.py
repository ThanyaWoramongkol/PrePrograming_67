"""Single Harvest Crops"""

def stardew():
    """-"""
    # input
    veg = input()
    time = int(input())
    price = int(input())
    amount = int(input())
    date = int(input())

    # condition
    if 28 - date > time + 1:
        print(f"The {veg} will be harvesrable on day {date + time} of the Season")
        print(f"Your income will be {amount * price:,} G")
    else:
        print(f"The Season will end before you can harvest your {veg}")
        print("Your income will be 0 G")

stardew()
