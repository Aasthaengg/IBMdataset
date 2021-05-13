s = input()
new_s = ""

for i in s:
    if i == "0" or i == "1":
        new_s += i
    else:
        new_s = new_s[:-1]
print(new_s)