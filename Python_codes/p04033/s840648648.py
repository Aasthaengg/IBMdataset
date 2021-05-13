a,b=map(int,input().split())
if a<=0 and b>=0:
    print("Zero")
    exit()
if a>0:
    print("Positive")
    exit()
tmp=0
for i in range(a,b+1):
    tmp+=1
if tmp%2==0:
    print("Positive")
else:
    print("Negative")