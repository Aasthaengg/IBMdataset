# スペース区切りの整数の入力
n, l = map(int, input().split())

data = []
for i in range(n):
    data.append(input())

l = sorted(data)
ans = ''

for i in range(n):
    ans += l[i]

print(ans)