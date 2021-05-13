s=input()
pr=True
if (s.count("N")==0)^(s.count("S")==0):
  pr=False
if (s.count("E")==0)^(s.count("W")==0):
  pr=False

if pr:
  print("Yes")
else:
  print("No")