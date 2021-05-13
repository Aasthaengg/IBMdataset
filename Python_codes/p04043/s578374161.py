data=list(map(int, input().split(" ")))
if (data.count(5)==2) and (data.count(7)==1):
  print('YES')
else:
  print('NO')