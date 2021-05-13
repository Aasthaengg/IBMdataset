a,b=map(int,input().split())

if a<0 and b<0:
    aa=a%2
    bb=b%2

    if (aa+bb)%2==1:
        print("Positive")
    else:
        print("Negative")
    exit()

if a<=0 and 0<=b:
    print("Zero")
    exit()

if 0<a and 0<b:
    print("Positive")
    exit()
