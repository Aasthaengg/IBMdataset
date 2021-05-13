A, B, C=list(map(int, input().split(" ")))
if ([A, B, C].count(5)==2) and ([A, B, C].count(7)==1):
  print('YES')
else:
  print('NO')
