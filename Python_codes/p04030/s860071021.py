zla=list(input())
s=[]
for i in zla:
    if i=='0':
        s.append('0')
    elif i=='1':
        s.append('1')
    elif i=='B':
        if s==[]:
            pass
        else:
            s.pop()

print(''.join(s))
