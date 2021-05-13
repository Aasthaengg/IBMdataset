arr = input()
new = ""
for x in arr:
    if x == "B":
        if new:
            new = new[:-1]
    else:
        new += x
print(new)
