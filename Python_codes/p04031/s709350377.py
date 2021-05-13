N  =int(input())
a = list(map(int,input().split()))
ans = (10**9)
for av in range(min(a),max(a)+1):
    Sum = 0
    for i in range(N):
        Sum += (a[i]-av)**2
    if Sum < ans:
        ans = Sum
print(ans)