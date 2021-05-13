S = input()

moved = {"N": False, "W": False, "S": False, "E": False}
for s in S:
    if not moved[s]:
        moved[s] = True

if (moved["N"] and moved["S"]) or not (moved["N"] or moved["S"]):
    if (moved["W"] and moved["E"]) or not (moved["W"] or moved["E"]):
        print("Yes")
    else:
        print("No")
else:
    print("No")