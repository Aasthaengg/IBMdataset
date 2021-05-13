#入力
lst = input().split()
 
#整数値化
for i in range(len(lst)):
  lst[i] = int(lst[i])
 
#ソート
lst.sort()
 
#出力
if lst == [5, 5, 7]:
  print('YES')
else:
  print('NO')