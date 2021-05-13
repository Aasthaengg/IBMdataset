N=int(input())
a=list(map(int,input().split()))
def change(a,x):
    sum=0
    for i in a:
        sum+=(x-i)**2
    return sum

def binarysearch(left,right,a):
    if right-left<=1:
        return min(change(a,left),change(a,right))
    else:
        center=left+(right-left)//2
        if change(a,center)<=change(a,center+1):
            return binarysearch(left,center,a)
        else:
            return binarysearch(center,right,a)

if change(a,100)<=change(a,99):
    print(change(a,100))
elif change(a,-100)<=change(a,-99):
    print(change(a,-100))
else:
    print(binarysearch(-100,100,a))