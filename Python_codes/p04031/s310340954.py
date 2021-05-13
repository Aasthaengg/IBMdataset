from sys import stdin

def S(): return stdin.readline().rstrip()
def I(): return int(stdin.readline().rstrip())
def LS(): return list(stdin.readline().rstrip().split())
def LI(): return list(map(int,stdin.readline().rstrip().split()))

def cost(x,y):
    return pow(x-y,2)
n = I()
a = LI()

sum = 0
for i in range(n):
    sum += a[i]

ave = round(sum/n)
if ave+0.5 <= sum/n:
    ave += 1

ans = 0
for i in range(n):
    ans += cost(a[i],ave)

print(ans)