x,y=map(int,input().split())
if(x==0 or y==0):
    print('Zero')
elif(x>0 and y>0):
    print('Positive')
elif(x<=0 and y>=0):
    print("Zero")
else:
    z=abs(y-x)
    if(z%2==0):
        print("Negative")
    else:
        print("Positive")

