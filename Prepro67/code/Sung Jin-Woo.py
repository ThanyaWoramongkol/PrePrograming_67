"""Sung Jin-Woo"""

def main(level):
    """-"""
    current_lv = level
    level_up = level ** 2 + 1000
    exp_get = 0
    exp = ""
    while exp != "End":
        exp = input()
        if exp == "End":
            break
        exp_get += int(exp)
    current_exp = exp_get
    while current_exp > level_up:
        current_exp -= level_up
        level_up = current_lv ** 2 + 1000
        current_lv += 1
    print(f"Exp gained : {exp_get}\n{current_lv - level} Level up, Now you are level {current_lv}")

main(int(input()))
