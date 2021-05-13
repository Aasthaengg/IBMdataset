import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

a, b = inintm()

if a <= 0 and b >= 0:
    print("Zero")
elif a < 0 and b < 0:
    if (abs(a) - abs(b)) % 2 == 0:
        print("Negative")
    else:
        print("Positive")
else:
    print("Positive")