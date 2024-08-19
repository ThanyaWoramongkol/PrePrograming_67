"""Arithmetic progression Building"""

def main(dr, step, start, stop):
    """-"""
    storage = str(start)
    output = ""
    for _ in range(start, stop+1):
        if dr == "d":
            start += step
            storage += str(start)
        else:
            start *= step
            storage += str(start)
    for i in storage:
        output += f'[ {i} ]'
    print(output)
main(input(), int(input()), int(input()), int(input()))
