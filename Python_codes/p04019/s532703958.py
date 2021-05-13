S = list(input())
flag = 1
if "S" in S:
  if not("N" in S):
    flag = 0
if "N" in S:
  if not("S" in S):
    flag = 0
if "E" in S:
  if not("W" in S):
    flag = 0
if "W" in S:
  if not("E" in S):
    flag = 0
if flag:
  print("Yes")
else:
  print("No")
