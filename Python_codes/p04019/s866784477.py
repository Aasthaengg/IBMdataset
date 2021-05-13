s = input()
count = {"N":0, "W":0, "S":0, "E":0}
for i in s:
    count[i] += 1

if ((count["N"] != 0 and count["S"] != 0) or (count["N"] == count["S"] == 0))and ((count["W"] != 0 and count["E"] != 0) or (count["W"] == count["E"] == 0)):
    print("Yes")

else:
    print("No")
