S = input().strip()
C = {"N":0,"S":0,"E":0,"W":0}
for i in range(len(S)):
    C[S[i]] += 1
if C["N"]>0 and C["S"]>0:
    if (C["E"]>0 and C["W"]>0) or (C["E"]==0 and C["W"]==0):
        print("Yes")
    else:
        print("No")
elif C["N"]==0 and C["S"]==0:
    if (C["E"]>0 and C["W"]>0) or (C["E"]==0 and C["W"]==0):
        print("Yes")
    else:
        print("No")
else:
    print("No")