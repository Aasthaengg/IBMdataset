w = input()
d = dict()
flag = 0
for i in w:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
for k,v in d.items():
    if v%2==0:
        flag=1
    else:
        flag=0
        break
if flag==1:
    print("Yes")
else:
    print("No")
