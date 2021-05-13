s = list(input())
ans = 1
cE = s.count("E")
cW = s.count("W")
cS = s.count("S")
cN = s.count("N")
if cE >=1:
    if cW == 0:
        ans = 0
if cW >=1:
    if cE == 0:
        ans = 0
if cN >=1:
    if cS == 0:
        ans = 0
if cS >=1:
    if cN == 0:
        ans = 0
if ans == 1:
    print("Yes")
else:
    print("No")