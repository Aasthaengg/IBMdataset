n=int(input())
a=[int(input())for i in range(n)]
c=0
l=[]
l2=[]
for i in a:
    if i!=0:
        l.append(i)
    else:
        l2.append(sum(l)//2)
        l=[]
l2.append(sum(l)//2)
print(sum(l2))