import sys
input = sys.stdin.readline
n,m = map(int,input().split())
hako = [1]*(n+1)
iro = ['white']*(n+1)
iro[1] = 'red'

for _ in range(m):
    
    x,y = map(int,input().split())
    if iro[x] == 'red':
        iro[y] ='red'
    elif iro[x] == 'white' and hako[y] == 0:
        iro[y] = 'white'
    hako[x] -= 1
    hako[y] += 1
ans = 0
for i in range(1,n+1):
    if hako[i] > 0 and iro[i] == 'red':
        ans += 1
print(ans)