"""Emote"""

def main(feeling, text):
    """-"""
    acting = ("Tired", "Sad", "Happy", "Angry", "Shy")
    if feeling in acting:
        if feeling == acting[0]:
            print(f'"{text}"\n(=_=)')
        elif feeling == acting[1]:
            print(f">>'{text}'<<\n\\ToT/")
        elif feeling == acting[2]:
            print(f'\\\\"{text}"//\n(^o^)')
        elif feeling == acting[3]:
            print(f"!!!'{text}'!!!\n(*O_O*)")
        else:
            print(f'<"\'{text}\'">\n(^///^)')
    else:
        print("\\'?'/")

main(input(), input())
