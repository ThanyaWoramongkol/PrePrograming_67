"""Taxi V1"""

def ichi(kilometer):
    """2 => 10"""
    return kilometer * 6.5

def juu(kilometer):
    """11 => 20"""
    return kilometer * 7

def nijuu(kilometer):
    """21 km => 40 km"""
    return kilometer * 8

def yonjuu(kilometer):
    """41 km => 60 km"""
    return kilometer * 8.5

def rokujuu(kilometer):
    """61 km => 80 km"""
    return kilometer * 9

def hachijuu(kilometer):
    """ >= 81 km"""
    return kilometer * 10.5

def main(distance):
    """-"""
    if distance > 80:
        cost = 35 + ichi(9) + juu(10) + nijuu(20) + yonjuu(20) \
        + rokujuu(20) + hachijuu(distance - 80)
    elif distance > 60:
        cost = 35 + ichi(9) + juu(10) + nijuu(20) + yonjuu(20) \
        + rokujuu(distance - 60)
    elif distance > 40:
        cost = 35 + ichi(9) + juu(10) + nijuu(20) + yonjuu(distance - 40)
    elif distance > 20:
        cost = 35 + ichi(9) + juu(10) + nijuu(distance - 20)
    elif distance > 10:
        cost = 35 + ichi(9) + juu(distance - 10)
    elif distance > 1:
        cost = 35 + ichi(distance - 1)
    else:
        cost = 35
    return cost

print(f"{main(int(input())):.2f}")
