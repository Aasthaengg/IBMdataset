s = input()
ans = ''
for si in s:
  if si=='0': ans+='0'
  elif si=='1': ans+='1'
  else: ans=ans[:-1]
print(ans)