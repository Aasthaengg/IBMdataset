S=list(input())
ans=str()
for i in S:
  if i=="0":
    ans+="0"
  elif i=="1":
    ans+="1"
  else:
    if ans!="":
      ans=ans[:-1]
print(ans)