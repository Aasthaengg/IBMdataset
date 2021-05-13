n = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)
ans = 0
for i, l in enumerate(L):
    if i%2 == 1:
        ans += l
print(ans)
