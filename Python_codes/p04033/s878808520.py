a,b = map(int,input().split())
if b<0 and (b-a+1)%2==0:
    print("Positive")
elif b<0 and (b-a+1)%2==1:
    print("Negative")
elif a<0 and b>=0:
    print("Zero")
elif a==0:
    print("Zero")
elif a>0:
    print("Positive")