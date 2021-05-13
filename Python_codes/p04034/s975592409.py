n,m=map(int,input().split())

p=[1]*n
c=['w']*n
c[0]='r'


def ope(x,y):
    if c[x-1]=='r':
        c[y-1]='r'
    p[x-1] -= 1
    p[y-1] += 1
    if p[x-1]==0:
        c[x-1]='w'

for i in range(m):
    x,y=map(int,input().split())
    ope(x,y)


print(c.count('r'))
