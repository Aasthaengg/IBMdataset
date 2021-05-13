S = input ()
s = ''
for i in S:
  if i == '0':
    s += i
  elif i == '1':
    s += i
  elif i == 'B':
    if s != '':
      s = s[:-1]
print (s)