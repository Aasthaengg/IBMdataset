N = int(input())
a = [int(i) for i in input().split()]
ans = float("inf")
for i in range(-100, 101):
    ans = min(sum([(n - i)** 2 for n in a]), ans)
print(ans)