s=[]
a=list(input())

for i in a:
    if i=='0':
        s.append('0')
    elif i=='1':
        s.append('1')
    else:
        if len(s)==0:
            pass
        else:
            s.pop()

b="".join(s)
print(b)