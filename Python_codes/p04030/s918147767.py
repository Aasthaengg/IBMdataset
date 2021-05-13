def key():
    a=input()
    b=''
    for i in range(0,len(a)):
        if a[i]=='0':
            b+='0'
        elif a[i]=='1':
            b+='1'
        elif a[i]=='B':
            if len(b)==0:
                continue
            else:
                b=b[0:-1]
    print(b)

key()
