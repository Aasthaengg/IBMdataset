n, l = map(int, input().split())
sl = []
for i in range(n):
    s = input()
    sl.append(s)
sl.sort()
#print(sl)
ans = ""
for i in range(n):
    ans += sl[i]
print(ans)