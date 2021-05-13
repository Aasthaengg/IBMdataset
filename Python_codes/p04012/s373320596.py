from collections import *
s=input()
c=Counter(s)
f=0
for i in list(c.values()):
    if(i%2==1):
        f=1
        break
if(f==0):
    print('Yes')
else:
    print('No')
