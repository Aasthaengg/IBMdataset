def neg(a,b):
    n = max(a,b)-min(a,b)+1
    print('Negative' if n%2 else 'Positive')
    
def sign(a, b):
    if a==0 or b==0:
        print('Zero');        return
    sa =-1 if a*(-1) == abs(a) else 1
    sb =-1 if b*(-1) == abs(b) else 1
    if sa * sb == -1:
        print('Zero');        return
    elif sa==sb==1:
        print('Positive');        return
    else:
        neg(a,b)
        
a, b = map(int,input().split())
sign(a,b)