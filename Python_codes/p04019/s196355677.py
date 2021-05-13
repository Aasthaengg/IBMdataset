S=input()

D={s:False for s in ["N","W","S","E"]}

for s in S:
    D[s]=True

if (D["N"]==D["S"]) and (D["W"]==D["E"]):
    print("Yes")
else:
    print("No")
