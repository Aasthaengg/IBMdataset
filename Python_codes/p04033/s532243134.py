a,b=map(int,input().split(' '))
if a<=0<=b:
    print("Zero")
elif a > 0 or (abs(b-a)%2!=0):
    print("Positive")
else:
    print("Negative")