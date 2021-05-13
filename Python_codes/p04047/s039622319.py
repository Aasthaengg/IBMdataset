N = int(input())
L = sorted(map(int, input().split()))

ans = sum(L[::2])

print(ans)