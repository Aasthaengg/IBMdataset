def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b = iim()

if a*b <= 0:
    print('Zero')
elif a > 0:
    print('Positive')
else:
    if abs(a-b)%2 == 0:
        print('Negative')
    else:
        print('Positive')