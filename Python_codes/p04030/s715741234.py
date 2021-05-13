S = input()

ret = ""
for i in S:
    if i != "B":
        ret += i
    else:
        ret = ret[:-1]

print(ret)