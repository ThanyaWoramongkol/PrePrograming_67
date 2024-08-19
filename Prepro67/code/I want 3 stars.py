"""I want 3 stars!"""

def main(jumnuan):
    """-"""
    if jumnuan % 9:
        print(f"You need {9 - jumnuan} more to get 3 stars champion.")
    else:
        print("Success! You created a 3 stars champion!")
main(int(input()))
