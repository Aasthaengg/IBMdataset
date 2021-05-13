import sys
from math import pi

def solve():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    if A <= 0 <= B: print("Zero")
    elif 0 < A: print("Positive")
    else:
        if (min(-1, B) - A) % 2 == 1: print("Positive")
        else: print("Negative")
    

    return 0

if __name__ == "__main__":
    solve()