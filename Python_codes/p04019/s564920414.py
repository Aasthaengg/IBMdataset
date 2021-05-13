S = input()

if (S.count("W")>0 and S.count("E")==0) or (S.count("E")>0 and S.count("W")==0) or (S.count("N")>0 and S.count("S")==0) or (S.count("S")>0 and S.count("N")==0):  print("No")
else:
  print("Yes")