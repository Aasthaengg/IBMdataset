lst = sorted(list(map(int, input().split())))

if lst[-1] == 7 and lst[0] == 5 and lst[1] == 5:
  print('YES')
else:
  print('NO')
