s = list(input())
ew = []
sn = []
for i in s:
    if i == "E" or i == "W":
        ew.append(i)
    else:
        sn.append(i)
if len(set(ew)) == 1 or len(set(sn)) == 1:
    print("No")
else:
    print("Yes")