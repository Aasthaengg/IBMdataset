n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
ans = 0
cnt = 0
for i in a:
    if i==0:
        ans += cnt//2
        cnt = 0
    else:
        cnt += i
ans += cnt//2
print(ans)