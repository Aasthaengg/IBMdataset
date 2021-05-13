s=str(input())
C= list(s)
list=[]
for I in range(len(C)):
    if C[I]!='B':
        list.append(C[I])
    elif C[I]=='B' and len(list)!=0:
        list.pop()
 
print("".join(list))