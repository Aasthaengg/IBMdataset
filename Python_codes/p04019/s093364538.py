import sys
from collections import Counter

tmp = sys.stdin.readline().strip()
directions = ""
pre = ""
for c in tmp:
    if c == pre:
        continue
    directions += c
    pre = c
    
counter = Counter(directions)
# print(counter)

d = {"S": 0, "E": 0, "N": 0, "W": 0}
for t, count in counter.items():
    d[t] = count

sn = False
if 0 < d["S"] and 0 < d["N"] and abs(d["S"] - d["N"]) < 2:
    sn = True
if d["S"] == d["N"]:
    sn = True

ew = False
if 0 < d["E"] and 0 < d["W"] and abs(d["E"] - d["W"]) < 2:
    ew = True
if d["E"] == d["W"]:
    ew = True

if sn and ew:
    print("Yes")
else:
    print("No")