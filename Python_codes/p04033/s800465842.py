a,b=map(int,input().split())
if a<=0<=b:
    print ("Zero")
elif (min(0,b)-a)%2:
    print ("Positive")
else:
    print ("Negative")