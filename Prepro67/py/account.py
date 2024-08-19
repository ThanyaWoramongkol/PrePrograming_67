"""Account"""

def main():
    """-"""
    account = 500
    withdraw = 200
    while account >= 0:
        if withdraw > account:
            print("Not enough money.")
            break
        account -= withdraw
        print(f"The account has {account} Baht.")
    print(f"The account has {account} Baht.")
main()
