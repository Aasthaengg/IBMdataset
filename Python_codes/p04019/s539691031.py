S = input()
count = {s: 0 for s in "NWSE"}
for s in S:
    count[s] += 1

if count["N"] == 0 and count["S"] >= 1 or count["N"] >= 1 and count["S"] == 0:
    print("No")
elif count["E"] == 0 and count["W"] >= 1 or count["E"] >= 1 and count["W"] == 0:
    print("No")
else:
    print("Yes")