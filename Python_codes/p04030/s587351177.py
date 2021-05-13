s=input()
l=[]
for i in s:
  if i=="0":
    l.append("0")
  elif i=="1":
    l.append("1")
  elif i=="B":
    if l!=[]:
    	l.pop()
if l==[]:
  print("")
else:
  print("".join(l))
