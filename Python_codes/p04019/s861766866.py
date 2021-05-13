import collections
S=str(input())

List=list(set(S))
List.sort()

flag=0
if len(List)%2==0:
    if len(List)//2==1:
        if List[0]=="E" and List[1]=="W":
            flag=1
        elif List[0]=="N" and List[1]=="S":
            flag=1
    elif len(List)//2==2:
            flag=1
            
print("Yes" if flag==1 else "No")