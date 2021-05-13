N, L = map(int,input().split())
a = []
for i in range(N):
    a.append(input())
a.sort()
ans= ''
for i in a:
    ans += i
print(ans)
