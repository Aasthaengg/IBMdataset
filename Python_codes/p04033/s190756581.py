import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    a, b = [int(x) for x in input().rstrip().split(" ")]

    if(a > 0):
        print("Positive")
    elif(a == 0 or b == 0):
        print("Zero")
    elif(a < 0 and 0 < b):
        print("Zero")
    else:
        num = b - a + 1
        if num % 2 == 0:
            print("Positive")
        else:
            print("Negative")



if __name__ == "__main__":
    resolve()
