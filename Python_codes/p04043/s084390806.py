a=str(input())
alist=list(a)
count7=0
count5=0
for x in alist:
    if x=="7":
        count7+=1
    if x=="5":
        count5+=1
    else:
        pass
if count7==1 and count5==2:
    print("YES")
else:
    print("NO")