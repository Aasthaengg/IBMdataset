import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
lis = []
for s in S:
    if s=='0':
        lis.append(str(0))
    if s=='1':
        lis.append(str(1))
    if s=='B':
        if len(lis):
            lis.pop()

print(''.join(lis))