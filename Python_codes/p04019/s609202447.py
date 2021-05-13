S=input()
n=0
s=0
w=0
e=0
for i in range(len(S)):
    if S[i]=="N":
        n+=1
    if S[i]=="S":
        s+=1
    if S[i]=="W":
        w+=1
    if S[i]=="E":
        e+=1

if n!=0 and s!=0 and w!=0 and e!=0 or n==0 and s==0 and w!=0 and e!=0 or n!=0 and s!=0 and w==0 and e==0:
    print("Yes")

else:
    print("No")
    
