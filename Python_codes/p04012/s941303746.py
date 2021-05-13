s=input()
d={}
for i in s:
  d[i]=d.get(i,0)+1
for i in set(s):
  if d[i]%2==1:
    print("No")
    break
else:
  print("Yes")