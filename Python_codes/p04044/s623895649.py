N,L = map(int,input().split())
moji = []
for i in range(N):
    moji.append(input())
sort_moji = sorted(moji)
ans = ''
for i in sort_moji:
    ans += i
print(ans)