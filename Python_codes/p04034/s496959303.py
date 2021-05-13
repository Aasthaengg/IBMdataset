# 2020/08/09
# AtCoder Grand Contest 002 - A

# Input
n, m = map(int,input().split())
rlist = [0] * (n+1)
wlist = [1] * (n+1) 
rlist[1] = 1
wlist[1] = 0

# Calc
for i in range(m):
    x, y = map(int,input().split())
    if rlist[x] >= 1:
        rlist[y] = rlist[y] + 1
        # if rlist[x] == 1 and wlist[x] == 0:
        if wlist[x] == 0:
            rlist[x] = rlist[x] - 1
        else:
            wlist[x] = wlist[x] - 1
    else:
        wlist[y] = wlist[y] + 1
        wlist[x] = wlist[x] - 1

ans = 0
for i in range(n+1):
    if rlist[i] >= 1:
        ans = ans + 1

# Output
print(ans)
