s=list(input())
x=[]
for i in s:
  if i=="0" or i=="1":
    x.append(i)
  else :
    if not x:
      pass
    else:
   	  del x[-1]
print("".join(x))