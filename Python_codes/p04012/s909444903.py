w=input()

dict={}
alh="abcdefghijklmnopqrstuvwxyz"
for i in alh:
  dict[i]=0
for i in w:
  dict[i]+=1
flag=True
for i in alh:
  if dict[i]%2==1:
    flag=False
if flag:
  print("Yes")
else:
  print("No")