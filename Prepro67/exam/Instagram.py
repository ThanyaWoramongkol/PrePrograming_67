"""Instagram"""

def main(follower, followed):
    """-"""
    if abs(follower - followed) <= 10:
        print("related")
    elif abs(follower - followed) <= 100:
        print("almost related")
    else:
        print("not related")
main(int(input()), int(input()))
