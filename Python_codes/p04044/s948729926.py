n, l = map(int, input().split())
s = list()
for i in range(n):
    s.append(str(input()))
s.sort()
ans = ''
for j in range(n):
    ans = ans + s[j]
print(ans)