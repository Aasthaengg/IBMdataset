s = str(input())
a = ''
for i in s:
    if i == '0':
        a += '0'
    elif i == '1':
        a += '1'
    else:
        if len(a) != 0:
            a = a[:-1]
print(a)