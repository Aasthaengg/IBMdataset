r = []
for i in input():
    if 'B' == i:
        if r:
            r.pop()
    else:
        r.append(i)
print(''.join(r))