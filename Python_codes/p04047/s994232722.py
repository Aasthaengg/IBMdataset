N = int(input())
a = list(int(i) for i in input().split())
list.sort(a, reverse=True)
ans = 0
for i in range(N*2):
    if i%2 == 1:
        ans += a[i]
print(ans)