n = int(input())
lar, l = [], []
for i in range(n):
    a = int(input())
    if a == 0:
        lar.append(l)
        l = []
    else:
        l.append(a)
lar.append(l)
ans = 0
for l in lar:
    ans += sum(l) // 2
print(ans)