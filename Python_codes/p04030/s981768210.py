s=input()
t=''
for i in s:
  if i!='B':
    t+=i
  else:
    if t!='':
      t=t[:-1]
print(t)