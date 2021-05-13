n = int(input())
a = list(map(int, input().split()))
ans = float('inf')
for i in range(-100, 101):
    dummy = 0
    for a_i in a:
        dummy += pow((a_i-i), 2)
    ans = min(ans, dummy)
print(ans)