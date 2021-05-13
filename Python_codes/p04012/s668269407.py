import sys
w = input()
d = {}
for c in range(97,97+26):
    d[chr(c)]=0
for c in w:
    d[c]+=1

for c in d.values():
    if c%2 == 1:
        print("No")
        sys.exit()

print("Yes")