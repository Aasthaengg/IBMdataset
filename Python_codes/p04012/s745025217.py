w = list(input())
alpha = list("qwertyuiopasdfghjklzxcvbnm")
FLAG = True
for i in alpha:
  cnt = w.count(i)
  if cnt == 0:
    continue
  elif cnt % 2 == 0:
    continue
  else:
    print("No")
    FLAG = False
    break
while FLAG:
  print("Yes")
  break