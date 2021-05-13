s = list(input())
s = list(set(s))
flag = True
if "N" in s and not "S" in s:
    flag = False
if "S" in s and not "N" in s:
    flag = False
if "E" in s and not "W" in s:
    flag = False
if "W" in s and not "E" in s:
    flag = False
print("Yes" if flag else "No")