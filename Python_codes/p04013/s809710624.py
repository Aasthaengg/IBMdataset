n,a = map(int,input().split())
x = list(map(int,input().split()))

dpp = [0]*3000
dpm = [0]*3000

p = []
m = []
n0 = 0

for i in range(n):
    x1 = x[i] - a
    if x1 == 0:
        n0 += 1
    elif x1 > 0:
        p.append(x1)
    else:
        m.append(-x1)

for i in p:
    for j in range(2600,0,-1):
        if dpp[j] >= 1:
            dpp[j+i] += dpp[j]
    dpp[i] += 1

for i in m:
    for j in range(2600,0,-1):
        if dpm[j] >= 1:
            dpm[j+i] += dpm[j]
    dpm[i] += 1

ans = 0

for i in range(3000):
    ans += dpp[i] * dpm[i]

ans *= pow(2,n0)
ans += pow(2,n0) - 1

print(ans)
