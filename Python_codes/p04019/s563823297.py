S = list(input())
flag = True
if "N" in S:
  if "S" not in S:
    flag = False
if "S" in S:
  if "N" not in S:
    flag = False
if "E" in S:
  if "W" not in S:
    flag = False
if "W" in S:
  if "E" not in S:
    flag = False
if flag:
  print("Yes")
else:
  print("No")