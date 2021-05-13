printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n = inn()
a = [0]
for i in range(1,n+1):
    a.append(inn())
ddprint(a)
sm = 0
while len(a)>0:
    sm += a[-1]//2
    if len(a)>1 and a[-1]%2==1 and a[-2]>0:
        sm += 1
        a[-2] -= 1
    a.pop()
print(sm)
