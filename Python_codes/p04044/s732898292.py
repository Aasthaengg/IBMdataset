N, L = map(int, input().split())
S = sorted(list(input() for i in range(N)))
ans = str()
for i in range(N):
    ans += S[i]
print(ans)