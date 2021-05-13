s=list(input())
out=[]
for i in s:
  if i=="B":
    if out==[]:
      continue
    out.pop()
  else:
    out.append(i)
ou=""
for i in out:
  ou+=i
print(ou)