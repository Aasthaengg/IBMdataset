n,l=map(int,input().split())
arr=list(map(int,input().split()))
psbl=False
pos=0
for i in range(n-1):
    if arr[i]+arr[i+1]>=l:
        psbl=True
        pos=i
        break
if psbl:
    print("Possible")
    for i in range(0,pos):
        print(i+1)
    for i in range(n-2,pos,-1):
        print(i+1)
    print(pos+1)
else:
    print("Impossible")
