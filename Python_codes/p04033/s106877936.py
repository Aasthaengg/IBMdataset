a,b= list(map(int,input().split()))
if a==0 or b==0:
    print("Zero")
elif a>0 and b>0:
    print("Positive")
elif a<0 and b>0:
    print("Zero")
else:
    c = abs(b-a)
    if c%2 == 0:
        print("Negative")
    else:
        print("Positive")
