s=input()
a=s.count("N")
b=s.count("W")
c=s.count("S")
d=s.count("E")
ans=False
if a!=0 and c!=0:
    if (b!=0 and d!=0) or (b==0 and d==0):
        ans=True
if a==0 and c==0:
    if (b!=0 and d!=0) or (b==0 and d==0):
        ans=True
if ans==True:
    print("Yes")
else:
    print("No")