a,b=map(int,input().split())
if a>0:
    print("Positive")
elif a<0 and b>0:
    print("Zero")
else:
    if a%2 ==b%2:
        print("Negative")
    else:
        print("Positive")