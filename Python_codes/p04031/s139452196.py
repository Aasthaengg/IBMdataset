n = int(input())
a = list(map(int,input().split()))
ans = 1000000
a = sorted(a)
for i in range(a[0],a[n-1]+1):
    counter = 0
    for j in range(n):
        dif = abs(a[j] - i)
        dif *= dif
        counter += dif
    ans = min(ans,counter)
print(ans)