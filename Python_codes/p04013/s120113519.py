N,A = map(int,input().split())
X = list(map(int,input().split()))
ans = 0

def make_array(dims,fill):
    if len(dims) == 1:
        return [fill]*dims[0]
    ret = []
    nxt = dims[1:]
    for i in range(dims[0]):
        ret.append(make_array(nxt,fill))
    return ret
S = sum(X)+1
dp = make_array([N+2,N+2,S],0)
dp[0][0][0] = 1
for i in range(N):
    for j in range(N):
        for s in range(S-X[i]):
            dp[i+1][j+1][s+X[i]] += dp[i][j][s]
            dp[i+1][j][s] += dp[i][j][s]
ans = 0
for j in range(1,N+1):
    for s in range(1,S+1):
        if j*A == s:
            ans += dp[-2][j][s]
print(ans)