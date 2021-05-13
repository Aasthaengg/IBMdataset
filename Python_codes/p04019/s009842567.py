from collections import Counter


cntr = Counter(input())
x_ok, y_ok = False, False
if (cntr["E"] and cntr["W"]) or (not cntr["E"] and not cntr["W"]):
    x_ok = True
if (cntr["N"] and cntr["S"]) or (not cntr["N"] and not cntr["S"]):
    y_ok = True
print("Yes") if x_ok and y_ok else print("No")
