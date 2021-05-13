a,b= map(int,input().split())

if a==0 or b==0:
    print("Zero")
    exit()

if a<=0 and 0<=b:
    print("Zero")
    exit()

if b<0:
    a=abs(a)
    b=abs(b)
    res = a-b
    if res%2==0:
        print("Negative")
    else:
        print("Positive")
else:
    print("Positive")