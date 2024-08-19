"""What Time?"""

def calc(time, second):
    result = second // time
    return result, second - (result * time)

def main(second):
    """day:hr:min:sec"""
    day, second = calc(86400, second)
    hour, second = calc(3600, second)
    minute, second = calc(60, second)
    print(f"{day:02d}:{hour:02d}:{minute:02d}:{second:02d}")

main(int(input()))