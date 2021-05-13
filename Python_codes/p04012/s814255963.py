S = input()
count = dict()
for c in S:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

yes = True
for e in count.values():
    if e % 2 != 0:
        yes = False
        break
        
if yes:
    print("Yes")
else:
    print("No")