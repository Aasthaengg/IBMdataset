s = list(map(str, input()))
t = []
for i in s:
    if i != 'B':
        t.append(i)
    else:
        if len(t) > 0:
            t.pop(-1)
print(''.join(t))
