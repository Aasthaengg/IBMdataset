w = input()
d = {}
for i in range(len(w)):
  if w[i] not in d.keys():
    d[w[i]] = 1
  else:
    d[w[i]] += 1

for v in d.values():
  if v%2 != 0:
    print("No")
    exit()
print("Yes")
