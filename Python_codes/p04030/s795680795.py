s=input()
a=''

for i in s:
  if i=='B':
    a=a[:-1]
    
  else:
    a+=i
print(a)
