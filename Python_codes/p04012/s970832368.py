s = input()
check = 0
flag = True
for i in range(97,123):
  check =s.count(chr(i))
  if check % 2 == 1 :
    flag = False
if flag:
  print("Yes")
else:
  print("No")