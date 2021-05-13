w = input()
wl = list(w)
ws = set(w)
for i in ws:
  if wl.count(i) % 2 == 1:
    r = 'No'
    break
  else:
    r = 'Yes'
    
print(r)