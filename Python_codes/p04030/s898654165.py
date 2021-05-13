s=input()
l=[]
for i in s:
    if(i=='1'):
        l.append('1')
    elif(i=='0'):
        l.append('0')
    else:
        if(l!=[]):
            l.pop()
print(''.join(l))
