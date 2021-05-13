a = input()
dct ={}
for i in a:
    dct[i] = dct.get(i,0)+1
for i in dct.values():
    if i % 2 != 0:
        res = "No"
        break
    else:
        res = "Yes"
print(res)
