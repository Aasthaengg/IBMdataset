m=input().strip("\n").split(" ")
a,b=int(m[0]),int(m[1])
if a>0:
    print("Positive")
elif b<0:
    if (b-a)%2:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")