"""10 Year Inflation"""

def main(past, now):
    """-"""
    inflation = now / past
    print(f"The price has increased {inflation - 1:.4%} from 10 years ago.")
    print(f"In next 10 years price will be {now * inflation:.2f} baht.")

main(float(input()), float(input()))
