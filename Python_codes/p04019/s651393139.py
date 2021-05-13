t=input()
n=0
s=0
w=0
e=0
for i in range(int(len(t))):
    if t[i] =="N":
        n=1
    if t[i] =="S":
        s=1
    if t[i] =="E":
        e=1
    if t[i] =="W":
        w=1
if (w+e)%2==0 and (n+s)%2==0:
    print("Yes")
else:
    print("No") 