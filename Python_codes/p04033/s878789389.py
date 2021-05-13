a,b= list(map(int,input().split()))
if 0 < a:
    print("Positive")
    exit()
elif 0<=b and a<=0:
    print("Zero")
    exit()
elif b < 0:
    if abs(a-b)%2==0:
        print("Negative")
        exit()
    else:
        print("Positive")
        exit()