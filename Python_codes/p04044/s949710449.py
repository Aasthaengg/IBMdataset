n, l = map(int,input().split())
S = [input() for i in range(n)]
ans = ''
for i in range(n):
    ans += S.pop(S.index(min(S)))
print(ans)