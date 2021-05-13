a, b, c = map(int, input().split())
ls = [a,b,c]
five = 0
seven = 0
for data in ls:
  if data == 5:
    five += 1
  elif data == 7:
    seven += 1
if five == 2 and seven == 1:
  print('YES')
else:
  print('NO')