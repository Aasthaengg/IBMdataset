n = int(input())
a = list(map(int,input().split()))

ans = -100
tmp = 10**10

for i in range(-100, 101):
    t = 0
    for j in a:
        t += (j - i) ** 2
    if t < tmp:
        ans = i
        tmp = t

print(tmp)
