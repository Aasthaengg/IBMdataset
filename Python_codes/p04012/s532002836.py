w = input ()
while len(w) != 0:
  if (w.count(w[0]))%2 == 1:
    print ('No')
    x = 0
    break
  else:
    x = w[0]
    w = w.replace(x,'')
if x != 0:
  print ('Yes')