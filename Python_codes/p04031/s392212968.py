n = int(input())
# n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
# abc = [int(input()) for i in range(5)]
if min(a) == max(a):
    print(0)
    exit()

ans = (max(a)*max(a))*n
for i in range(min(a), max(a)+1):
    total = 0
    for j in range(n):
        total += (a[j]-i)*(a[j]-i)
    if total < ans:
        ans = total


print(ans)
