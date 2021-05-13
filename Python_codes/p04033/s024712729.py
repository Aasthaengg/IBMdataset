import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b=map(int, input().split())
    if a>0:
        print('Positive')
    elif a<=0 and b>=0:
        print('Zero')
    elif b<0 and (b-a)%2==0:
        print('Negative')
    else:
        print('Positive')
resolve()