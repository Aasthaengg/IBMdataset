s = input()
ss = set(s)

r = 'Yes'
for w in ss:
  if s.count(w) % 2 == 1:
    r = 'No'
    break
print(r)