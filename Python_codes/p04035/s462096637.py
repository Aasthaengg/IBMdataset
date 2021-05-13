import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, L = mapint()
As = list(mapint())

procces = []
for i in range(1, N):
    double = As[i-1]+As[i]
    if double>=L:
        last = i
        print('Possible')
        break
else:
    print('Impossible')
    exit()
for i in range(1, last):
    print(i)
for i in range(N-1, last-1, -1):
    print(i)