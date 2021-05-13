s = input(); a = b = c = d = 0
if "N" in s: a = 1
if "W" in s: b = 1
if "S" in s: c = 1
if "E" in s: d = 1
print("Yes") if a == c and b == d else print("No")