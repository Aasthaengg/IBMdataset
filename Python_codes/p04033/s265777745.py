#40
import sys
a,b = map(int,input().split())
cou = 0

if a<=0 and b>=0:
    print("Zero")
    sys.exit()
elif a>=0 and b<=0:
    print("Zero")
    sys.exit()
    
if a>0 and b>0:
    print("Positive")
    sys.exit()
else:
    cou = abs(b-a) +1
    if cou %2 == 0:
        print("Positive")
    else:
        print("Negative")
