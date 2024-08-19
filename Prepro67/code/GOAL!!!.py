"""GOAL!!!"""

def main(home, away):
    """-"""
    print("Draw!" if home == away else ("Home Win!" if home > away else "Away Win!"))

main(int(input()), int(input()))
