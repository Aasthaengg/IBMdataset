a=list(map(int,input().split()))
lst=[0,0]
for i in range(3):
    if a[i]==5:
        lst[0]+=1
    elif a[i]==7:
        lst[1]+=1
if lst[0]==2 and lst[1]==1:
    print("YES")
else:
    print("NO")