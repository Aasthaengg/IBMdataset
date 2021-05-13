a,b=map(int,input().split())
if a>=0:
    print("Positive" if a!=0 else "Zero")
if a<0 and b>0:
    print("Zero")
if b<=0:
    if b==0:
        print("Zero")
    else:
        if (a-b+1)%2==0:
            print("Positive")
        else:
            print("Negative")