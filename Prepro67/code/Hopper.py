"""Hopper"""

def meinkraft(jumnuan):
    """dictionary.items()"""
    hopper = {}
    for _ in range(jumnuan):
        item, amount = input(), int(input())
        if item not in hopper:
            hopper[item] = amount
        else:
            hopper[item] += amount
    print("My Hopper has a list item:")
    for items, count in hopper.items():
        print(f"{items} : {count}")
meinkraft(int(input()))
