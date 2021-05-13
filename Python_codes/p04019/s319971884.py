s=list(input())
m=set(s)
if len(m)==4:
  print("Yes")
elif len(m)==2:
  c1="S" in m and "N" in m
  c2="W" in m and "E" in m
  if c1 or c2:
    print("Yes")
  else:
    print("No")
else:
  print("No")