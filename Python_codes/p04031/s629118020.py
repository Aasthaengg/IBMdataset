N = int(input())
A = [int(x) for x in input().split()]
average = round(sum(A) / N)
ans = 0
for x in A: ans += (average-x)**2
print(ans)