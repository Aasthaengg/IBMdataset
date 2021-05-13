s=input()
ryoko={'S':False,'N':False,'W':False,'E':False}
for c in s:
    ryoko[c]=True
if (ryoko['S']!=ryoko['N']) or (ryoko['W']!=ryoko['E']):
    print('No')
else:
    print('Yes')
