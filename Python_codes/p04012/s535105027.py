D={}
W=input()

for w in W:
    if w in D:
        D[w]+=1
    else:
        D[w]=1

F=True
for a in D:
    F&=(D[a]%2==0)

if F:
    print("Yes")
else:
    print("No")
