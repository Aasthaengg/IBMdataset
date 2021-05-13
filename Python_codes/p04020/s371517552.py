n = int(input())
A = [int(input()) for _ in range(n)]
ans = 0
temp = 0
for i in range(n):
    ans += (A[i]+temp)//2
    if A[i] != 0:
        temp = (A[i]+temp)%2
    else:
        temp = 0
print(ans)