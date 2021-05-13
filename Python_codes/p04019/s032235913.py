s = input()
ok = True
if s.count("N") >= 1:
    if s.count("S") == 0:
        ok = False
if s.count("S") >= 1:
    if s.count("N") == 0:
        ok = False

if s.count("E") >= 1:
    if s.count("W") == 0:
        ok = False

if s.count("W") >= 1:
    if s.count("E") == 0:
        ok = False
if ok:
    print("Yes")
else:
    print("No")