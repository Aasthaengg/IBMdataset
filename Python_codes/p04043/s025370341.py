a, b, c = map(int, input().split())
if a == 5:
  if b == 5 and c == 7:
    print('YES')
  elif b == 7 and c == 5:
    print('YES')
  else:
    print('NO')
else:
  if b == 5 and c == 5:
    print('YES')
  else:
    print('NO')