import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = map(int, input().split())
c = [1]*n
r = set([0])
for i in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    if c[x]==1 and x in r:
        r.remove(x)
        r.add(y)
    elif c[x]>=2 and x in r:
        r.add(y)
    c[x] -= 1
    c[y] += 1
print(len(r))