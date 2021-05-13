n = input()
s = ''
for i in n:
    if i== '1' or i == '0':
        s+=i
    else:
        if len(s)>0:
            s =s[0:-1]
print(s)
