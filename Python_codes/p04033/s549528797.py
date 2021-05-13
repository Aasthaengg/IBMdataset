a,b=map(int,input().split())
if a*b<=0:
    print("Zero")
    exit()
if a>0:
    print("Positive")
else:
    if (b-a)%2==1:
        print("Positive")
    else:
        print("Negative")