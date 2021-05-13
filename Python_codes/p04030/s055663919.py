s = input()

list = []

for i in s:
    if i == "0":
        list.append(i)
    elif i == "1":
        list.append(i)
    elif i == "B" and list != []:
        list.pop(-1)
    else:
        continue

print("".join(list))