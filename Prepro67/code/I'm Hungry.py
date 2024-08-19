"""I'm hungry"""

def main(stat):
    """-"""
    if stat == "Not hungry":
        print("I'm fine.")
    else:
        chest = input()
        if chest == "Empty":
            print("There must be only one way left.")
        elif chest.count("Chicken"):
            print("I'd rather die than eat this.")
        else:
            print("I survived.")
main(input())
