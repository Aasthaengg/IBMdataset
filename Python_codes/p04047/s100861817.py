tc = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in arr[::2]:
    ans += i
print(ans)
