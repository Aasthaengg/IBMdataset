w=input()
data='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
  if w.count(data[i])%2==0:
    continue
  else:
    print('No')
    exit()
print('Yes')