S=input()
sn = "N" in S
se = "E" in S
ss = "S" in S
sw = "W" in S
if (sn==ss) and (se==sw):
  print("Yes")
else:
  print("No")