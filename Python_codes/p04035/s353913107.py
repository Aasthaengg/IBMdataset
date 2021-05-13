from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,l = inm()
a = inl()
for i in range(n-1):
    if a[i]+a[i+1]>=l:
        print('Possible')
        for j in range(i):
            print(j+1)
        for j in range(n-2,i-1,-1):
            print(j+1)
        exit()
print('Impossible')
