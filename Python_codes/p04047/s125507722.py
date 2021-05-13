import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
l = list(map(int, input().split()))
l.sort()
if len(l)%2==1:
    l = l[1:]
ans = 0
ans = sum(l[::2])
print(ans)