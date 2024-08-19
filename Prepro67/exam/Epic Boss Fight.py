"""Epic Boss Fight"""

def result(hp_boss, hp_player):
    """output result of this battle"""
    if not hp_player and not hp_boss:
        print("Huh?!")
    elif hp_player <= 0:
        print("No, I'm lose. ;-;")
    elif hp_boss <= 0:
        print("======================")
        print("Yeah! I'm Win!!")

def main(hp_boss, atk_boss, hp_player, atk_player):
    """-"""
    # zet max_hp and variable cooldown each of moves
    max_hp = hp_player
    skill_cd = 0
    ultimate_cd = 0
    heal_cd = 0
    print("======================")
    while hp_player > 0 and hp_boss > 0:
        action = input()

        # Start battle
        ultimate_cd -= 1
        skill_cd -= 1
        heal_cd -= 1

        # player turn
        if action == 'attack':
            hp_boss -= atk_player
            print('"Attack!"')
        elif action == 'skill' and skill_cd <= 0:
            hp_boss -= atk_player * 2
            skill_cd = 2
            print('"Skill!!"')
        elif action == 'heal' and heal_cd <= 0:
            hp_player += atk_player * 5
            heal_cd = 3
            if hp_player > max_hp:
                hp_player = max_hp
            print("Heal!!!")
        elif action == 'ultimate' and ultimate_cd <= 0:
            hp_boss -= atk_player * 5
            ultimate_cd = 5
            print('"ULTIMATEEE!!!!!"')
        else:
            print("No! I'm missed.")
        # zet cooldown when it under zero
        if skill_cd < 0:
            skill_cd = 0
        if ultimate_cd < 0:
            ultimate_cd = 0
        if heal_cd < 0:
            heal_cd = 0
        # condition check. Is player killed boss already?
        if hp_boss > 0 and hp_player > 0:
            # boss turn
            hp_player -= atk_boss
            if hp_player < 0:
                hp_player = 0
            # detail CD and HP
            print(f"Boss HP: {hp_boss} | Player HP: {hp_player}")
            print(f"Skill CD: {skill_cd} | Heal CD: {heal_cd} | Ultimate CD: {ultimate_cd}")
            print("======================")
    result(hp_boss, hp_player)
main(int(input()), int(input()), int(input()), int(input()))
