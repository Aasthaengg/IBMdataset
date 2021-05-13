import collections

s = input()

c = collections.Counter(s)
    
v = list(c.values())

for i in v:
    if i % 2 == 1:
        print("No")
        exit()
print("Yes")