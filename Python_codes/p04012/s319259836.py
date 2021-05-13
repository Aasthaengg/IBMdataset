s = input()
 
r = 'Yes'
for w in s:
  if s.count(w) % 2 == 1:
    r = 'No'
    break
print(r)