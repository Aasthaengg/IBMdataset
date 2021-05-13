import sys
a,b = map(int, input().split())
if a <= 0 <= b:
    print("Zero")
    sys.exit()
elif b <0 and (b-a+1)%2 == 1:
    print("Negative")
    sys.exit()
else:
    print("Positive")