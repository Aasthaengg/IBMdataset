n,m = map(int,input().split())
l = [list(map(int,input().split())) for i in range(m)]
x,y = [list(i) for i in zip(*l)]
num = [1] * n
red = ['out'] * n
red[0] = 'in'
for i in range(m):
    if red[x[i]-1] == 'in':
        red[y[i]-1] = 'in'
    num[x[i]-1] -= 1
    num[y[i]-1] += 1
    if num[x[i]-1] == 0:
        red[x[i]-1] = 'out'
print(red.count('in'))