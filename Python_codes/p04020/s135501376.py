n = int(input())
arr = [int(input()) for _ in range(n)]

ans = 0
for i in range(n):
    ans += arr[i] // 2
    arr[i] %= 2
    if i != n - 1:
        if arr[i] == 1 and arr[i + 1] >= 1:
            arr[i] -= 1
            arr[i + 1] -= 1
            ans += 1

print(ans)