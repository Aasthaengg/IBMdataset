n = int(input())
a = [int(input()) for _ in range(n)]

lsts = []
temp = []
for aa in a:
    if aa == 0:
        if temp:
            lsts.append(temp)
            temp = []
    else:
        temp.append(aa)
if temp: lsts.append(temp)

ans = 0

for lst in lsts:
    for i, aa in enumerate(lst):
        ans += aa // 2
        if i != len(lst)-1:
            lst[i+1] -= aa % 2
            ans += aa % 2

print(ans)