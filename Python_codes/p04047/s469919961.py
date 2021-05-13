import sys
input = sys.stdin.readline

n=int(input())
vA=list(map(int,input().split()))
vA.sort()
res=sum(a for a in vA[::2])

print(res)
