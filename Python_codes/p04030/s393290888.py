s = list(map(str, input()))
t = ''
for i in s:
    if i != 'B':
        t += i
    else:
        t = t[:-1]
print(t)
