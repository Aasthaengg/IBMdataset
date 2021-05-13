a,b=map(int,input().split())
if a>0 and b>0:
    print("Positive")
elif a<=0 and b>=0:
    print("Zero")
elif (abs(b-a)+1)%2==0:
    print("Positive")
elif (abs(b-a)+1)%2==1:
    print("Negative")