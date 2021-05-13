s1 = str(input())
s = []
for i in s1:
    if i == '0' or i == '1':
        s.append(i)
    else:
        if 1 <= len(s):
            s.pop(len(s)-1)
w = ""
for h in s:
    w += h
print(w)