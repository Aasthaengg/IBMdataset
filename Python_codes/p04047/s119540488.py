n = int(input())
L = sorted(map(int,input().split()))
ans = L[0::2]
ans = sum(ans)
print(ans)