a = list(map(int, input().split()))
cnt_5 = 0
cnt_7 = 0

for i in a:
  if i == 5:
    cnt_5 += 1
  if i == 7:
    cnt_7 += 1
      
if cnt_5 == 2 and cnt_7 == 1:
  print('YES')
else:
  print('NO')