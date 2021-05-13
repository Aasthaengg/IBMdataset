a,b=map(int,input().split())
import  sys

if b-a>=b and b>=0:
    print('Zero')
    sys.exit()

if a>0:
    print('Positive')
else:
    if len(range(a,b+1))%2==0:
       print('Positive')
    else:
        print('Negative')
