S = input().strip()
f = True
if S.count("N")*S.count("S") == 0 and S.count("N")+S.count("S") != 0:
    f = False
if S.count("E")*S.count("W") == 0 and S.count("E")+S.count("W") != 0:
    f = False
print("Yes" if f else "No")
