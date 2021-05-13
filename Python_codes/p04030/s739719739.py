s = input()

res = ""
for c in s:
    if c != "B":
        res = res + c
    else:
        res = res[:-1]
print(res)
