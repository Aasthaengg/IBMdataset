s=input()
ans=[]
for i in s:
  if i=="0":
    ans.append("0")
  elif i=="1":
    ans.append("1")
  else:
    if len(ans)>=1:
      ans.pop(len(ans)-1)
    else:
      continue
print("".join(ans))