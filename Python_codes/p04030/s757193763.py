def hi():
  a = input()
  key = ""
  for i in range(len(a)):
    if a[i]=='0':
      key += '0'
    elif a[i]=='1':
      key += '1'
    elif a[i]=='B':
      if len(key) == 0:
        continue
      else:
        key = key[0:-1]
  print(key)

hi()