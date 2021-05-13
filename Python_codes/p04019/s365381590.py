s = input()
nwse = [0]*4
for i in s:
  if i=="N":
    nwse[0] =1
  elif i=="W":
    nwse[1] =1
  elif i=="S":
    nwse[2]=1
  else:
    nwse[3]=1
    
    
if nwse[0]==nwse[2] and nwse[1]==nwse[3]:
  print("Yes")
else:
  print("No")