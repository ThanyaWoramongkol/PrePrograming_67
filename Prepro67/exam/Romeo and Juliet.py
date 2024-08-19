"""Romeo and Juliet"""

def main(hours, minutes):
    """-"""
    minutes = minutes - 15
    if minutes < 0:
        hours -= 1
        minutes = 60 + minutes
    if hours < 0:
        hours = 23
    print(f"{hours:02}:{minutes:02}")

main(int(input()), int(input()))
