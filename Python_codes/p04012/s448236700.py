import sys
from collections import Counter


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

w = input()

c = Counter(w)

for i in tuple(c):
    if c[i] % 2 == 1:
        print("No")
        exit()

print("Yes")
