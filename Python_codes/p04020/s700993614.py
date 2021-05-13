n = int(input())
temp = 0
ans = 0
for i in range(n):
    a = int(input())
    if a != 0:
        q, r = divmod(a+temp, 2)
        ans += q
        temp = r
    else:
        temp = 0
print(ans)
