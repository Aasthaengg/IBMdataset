n = int(input())
an = list(map(int, input().split()))
ans = float('inf')
for i in range(-100, 101):
    check = 0
    for a in an:
        check += (a-i)**2
    ans = min(ans, check)
print(ans)
