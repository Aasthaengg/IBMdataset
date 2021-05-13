s = str(input())
result = ""
res = []

for i in range(len(s)):
    if s[i] == "0":
        res.append("0")
    elif s[i] == "1":
        res.append("1")
    else:
        if len(res) > 1:
            del res[-1]
        elif len(res) == 1:
            res = []

for i in res:
    result += i

print(result)
