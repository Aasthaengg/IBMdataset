s=input()
 
ans=''
for x in s:
  if x!='B':
    ans+=x
  else:
    if x!='':
      ans=ans[:-1]
print(ans)