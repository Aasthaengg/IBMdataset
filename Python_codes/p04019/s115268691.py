S = input()

L = [0] * 4

for s in S:
  if s == "N":
    L[0] = 1
  elif s == "S":
    L[1] = 1
  elif s == "E":
    L[2] = 1
  elif s == "W":
    L[3] = 1

if L[0] == L[1] and L[2] == L[3]:
  print("Yes")
else:
  print("No")