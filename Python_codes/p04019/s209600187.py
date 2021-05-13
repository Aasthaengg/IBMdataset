S = input()
if S.count("S") >= 1 and S.count("W") >= 1 and S.count("E") >= 1 and S.count("N") >= 1:
  print("Yes")
elif S.count("S") >= 1 and S.count("W") == 0 and S.count("E") == 0 and S.count("N") >= 1:
  print("Yes")
elif S.count("S") == 0 and S.count("W") >= 1 and S.count("E") >= 1 and S.count("N") == 0:
  print("Yes")
else:
  print("No")
