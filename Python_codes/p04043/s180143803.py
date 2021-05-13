l = list(map(int, input().split()))
l.sort(reverse=True)
if l[0] == 7 and l[1] == 5 and l[2] == 5:
  print('YES')
else:
  print('NO')