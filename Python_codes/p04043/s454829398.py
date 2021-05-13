import sys
import math

#https://atcoder.jp/contests/agc008/submissions/15248942
sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))
a = inl()
five = 0
seven = 0
for c in a:
    if c == 5:
        five += 1
    elif c == 7:
        seven+= 1
if five == 2 and seven == 1:
    print("YES")
else:
    print("NO")
