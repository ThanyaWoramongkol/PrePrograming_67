"""IShowSpeed's Brother"""
def main(pos1, pos2, time):
    print(f"The Velocity is {(pos2 - pos1) / time:.2f} m/s")
main(float(input()), float(input()), float(input()))
