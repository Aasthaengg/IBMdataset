N,A = map(int,input().split())
X = list(map(int,input().split()))

Xp = [0]
Xm = [0]
Xz = 0
for x in X:
    if x-A > 0:
        Xp.append(x-A)
    elif x-A < 0:
        Xm.append(x-A)
    else:
        Xz += 1

DPp = [[0 for j in range(2501)] for i in range(len(Xp))]
DPm = [[0 for j in range(2501)] for i in range(len(Xm))]

DPp[0][0] = 1
DPm[0][0] = 1

for i in range(1,len(DPp)):
    x = Xp[i]
    for j in range(2501):
        if j >= x:
            DPp[i][j] = DPp[i-1][j] + DPp[i-1][j-x]
        else:
            DPp[i][j] = DPp[i-1][j]

for i in range(1,len(DPm)):
    x = -Xm[i]
    for j in range(2501):
        if j >= x:
            DPm[i][j] = DPm[i-1][j] + DPm[i-1][j-x]
        else:
            DPm[i][j] = DPm[i-1][j]

ans = 1

for j in range(1,2501):
    ans += DPp[len(DPp)-1][j]*DPm[len(DPm)-1][j]
ans = ans*pow(2,Xz) - 1
print(ans)
