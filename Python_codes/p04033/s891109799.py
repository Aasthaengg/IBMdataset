import sys
input = sys.stdin.buffer.readline
a,b=map(int,input().split())
if a>0:
    print("Positive")
    exit(0)
elif a<=0 and 0<=b:
    print("Zero")
    exit(0)
elif a<0 and b<0:
    num=b-a+1
    if num%2==0:
        print("Positive")
        exit(0)
    else:
        print("Negative")
        exit(0)