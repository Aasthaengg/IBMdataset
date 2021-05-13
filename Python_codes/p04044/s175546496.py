N, L = map(int,input().split())
w = [input() for i in range(N)]
ans = ""
s_w = sorted(w)
for i in range(N):
    ans += s_w[i]
print(ans)