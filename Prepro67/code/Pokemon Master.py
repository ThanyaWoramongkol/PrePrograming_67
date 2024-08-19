"""Pokemon Master"""

def multi_type(action, enemy):
    multiplier = {"zero": 0, "normal": 1, "weak": 0.5, "super": 2}
    """check and return multiplier what each type advantage or disadvantageous"""
    # get moves advantage or disadvantageous of player
    if action == "Crunch":
        table = {"weak": ["Fighting", "Dark", "Fairy"], "super": ["Psychic", "Ghost"]}
    elif action == "Fishious Rend":
        table = {"weak": ["Water", "Grass", "Dragon"], "super": ["Fire", "Ground", "Rock"]}
    elif action == "Leech Life":
        table = {"weak": ["Fire", "Fighting", "Poison", "Flying", "Rock", "Steel", "Fairy"], 
        "super": ["Grass", "Psychic", "Dark"]}
    elif action == "Earthquake":
        table = {"zero": ["Flying"], "weak": ["Water", "Bug"], 
        "super": ["Fire", "Electric", "Poison", "Rock", "Steel"]}

    # search what type of enemy when get attack
    for mul in table:
        if enemy in table[mul]:
            setter = mul
        else:
            setter = "normal"
    print(setter)

    return multiplier[setter]

def bonus_dmg(base_dmg, action):
    """Calculate All of Bonus dmg"""
    summary = 0
    strong_jaw = ("Crunch", "Fishious Rend")
    if action in strong_jaw:
        summary += base_dmg * 0.5
    if action == strong_jaw[1]:
        summary += base_dmg * 0.5
    return summary

def main(level, attack, defend, enemy_hp):
    """Player Type is water-dragon type"""
    # set Default value
    counter = 0
    index = 1
    health = 384
    # dict for type of enemy will change every turn
    multiplier = {"zero": 0, "normal": 1, "weak": 2, "super": 0.5, "yowaimo": 0.25}
    enemy_type = ("Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison" \
    , "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy")
    my_poke = {"normal": ("Normal", "Fighting", "Flying", "Poison", "Ground"
    ,"Rock", "Bug", "Ghost", "Grass", "Electric", "Psychic", "Ice", "Dark")
    ,"super": ("Dragon", "Fairy"), "weak": ("steel"), "yowaimo":("fire", "water")}
    # dict for player move: damage
    move = {"Crunch": 80, "Fishious Rend": 85, "Leech Life": 80, "Eartquake": 100}

    # attack until each one hp drop under zero
    while enemy_hp > 0 or health > 0:
        # break condition
        
        skill = input()
        enemy = enemy_type[counter % 18]
        counter += 1

        base_dmg = ((2 * level + 10) * (attack / defend) * move[skill] + 2)
        deal_dmg = (base_dmg + bonus_dmg(base_dmg, skill)) * multi_type(skill, enemy)
        print(base_dmg, deal_dmg)

        # เหลือเอาค่า deal_dmg และ my_poke มาใช้( มอนตีเราเป็นค่า instance + เจาะเกราะ )
        # minus enemy_hp by deal_dmg
        enemy_hp -= deal_dmg

        # enemy hit player
        advan = ""
        for type_ in my_poke:
            if enemy in type_:
                advan = type_
        if enemy_hp > 0:
            health -= 70 * multiplier[advan]
        
    if enemy_hp <= 0:
        pass
    elif health <= 0:
        pass


main(int(input()), int(input()), int(input()), int(input()))
