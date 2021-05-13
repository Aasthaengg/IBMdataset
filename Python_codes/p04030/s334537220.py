s=input()
ans=""
for i in s:
  if i == "1"or i=="0":
    ans+=i
  else:
    if len(ans)>0:
      ans=ans[0:-1]
print(ans)