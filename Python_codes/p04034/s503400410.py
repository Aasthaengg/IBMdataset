N, M = map(int, input().split())
XYs = [list(map(int, input().split())) for _ in range(M)]

flag = [0]*(N+1)
flag2 = [0]*(N+1)
flag[1] = 1
flag2[1] = 1
num = [1]*(N+1)

for xy in XYs:
  if flag2[xy[0]]==1 and flag[xy[0]]==1:
    flag[xy[0]]=0
    flag[xy[1]]=1
  elif flag[xy[0]]==1:
    flag[xy[1]]=1
  
  if flag2[xy[0]]==1 and num[xy[1]] == 0:
    flag2[xy[0]]=0
    flag2[xy[1]]=1
  else:
    flag2[xy[0]]=0
    flag2[xy[1]]=0
  num[xy[0]] -= 1
  num[xy[1]] += 1
  if num[xy[0]] == 0:
    flag[xy[0]] = 0
  
print(sum(flag))