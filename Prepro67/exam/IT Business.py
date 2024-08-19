"""IT Business"""

def main(account, wallet):
    """-"""
    error = 0
    while error < 3:
        busi = input()
        if busi == 'end':
            break

        action = busi[0]
        amount = float(busi[2:])

        if action == "D":
            if wallet < amount:
                error += 1
            else:
                account += amount
                wallet -= amount
        elif action == "W":
            if account < amount:
                error += 1
            else:
                account -= amount
                wallet += amount
        else:
            error += 1
        # print(account, wallet, error, sep=" | ")

    print(f"{account:.2f}\n{wallet:.2f}")

main(float(input()), float(input()))
