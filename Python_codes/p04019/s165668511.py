S=input()
nsflag=False
weflag=False
if(("N" in S and "S" in S)or("N" not in S and "S" not in S)):
  if(("W" in S and "E" in S)or("W" not in S and "E" not in S)):
    print("Yes")
    exit()
print("No")