a, b, c = input().split()
LIST = [a, b, c]
five = LIST.count("5")
seven = LIST.count("7")
if five == 2 and seven == 1:
  print("YES")
else:
  print("NO")