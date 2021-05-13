S = input()
NS = set()
EW = set()
for s in S:
  if s in ["N", "S"]:
    NS.add(s)
  if s in ["E", "W"]:
    EW.add(s)
if len(NS) == 1 or len(EW) == 1:
  print("No")
else:
  print("Yes")