N, L = map(int, input().split())
S = ["" for _ in range(N)]
for i in range(N):
    S[i] = input()
S = sorted(S)

ans = ""
for i in range(len(S)):
    ans += S[i]
print(ans)
