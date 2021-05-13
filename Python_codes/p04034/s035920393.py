n,m = [int(x) for x in input().split()]
x = []
for i in range(m):
  x.append([int(x) for x in input().split()])
count = [1] * (n+1)
flag = [0] * (n+1)
flag[1] = 1
for i in range(m):
  if flag[x[i][0]] == 1:
    flag[x[i][1]] = 1
  if count[x[i][0]] == 1:
    flag[x[i][0]] = 0
  count[x[i][0]] -= 1
  count[x[i][1]] += 1

res = 0
for i in range(n+1):
  if flag[i] == 1:
    res += 1
    
print(res)