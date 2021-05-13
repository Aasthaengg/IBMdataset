s = str(input())
a = []

for i in s:
    if i == '0':
        a.append('0') 
    elif i == '1':
        a.append('1')
    elif i == 'B':
        if len(a) ==0:
            continue
        else:
            del a[-1]
        

print(''.join(a))