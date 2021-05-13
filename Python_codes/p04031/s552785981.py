n = int(input())
A = [int(i) for i in input().split()]
ave = round(sum(A) / n)
ans = 0
for x in A:
    ans += (x-ave)**2
print(ans)