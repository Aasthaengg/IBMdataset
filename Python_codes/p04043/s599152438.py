a = list(map(int, input().split()))

counter_5 = 0
counter_7 = 0

for i in range(len(a)):
  if a[i] == 5:
    counter_5 += 1
  if a[i]== 7:
    counter_7 += 1

if counter_5 == 2 and counter_7 ==1:
  print('YES')
else:
  print('NO')