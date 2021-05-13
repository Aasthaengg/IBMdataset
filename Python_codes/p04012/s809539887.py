import collections

w = input()
C = collections.Counter(w).values()

for c in C:
  if c%2==0:
    pass
  else:
    print("No")
    exit()
    
print("Yes")