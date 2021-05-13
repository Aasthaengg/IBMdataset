list = list(map(int,input().split()))

five = 0
seven = 0

for i in list:
  if i == 5:
    five += 1
  elif i == 7:
    seven += 1
  else:
      pass

if seven == 1 and five == 2:
  print("YES")
else:
    print("NO")