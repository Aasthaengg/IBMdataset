t=input()
n='N' in t
w='W' in t
s='S' in t
e='E' in t

if n==s and w==e:
    print('Yes')
else:
    print('No')