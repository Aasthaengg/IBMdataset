n,m  = map(int,input().split())

balls = [1 for _ in range(n)]
red = [1] + [0 for _ in range(1,n)]

for _ in range(m):
  x, y = map(int,input().split())
  x,y = x-1, y-1
  
  if balls[x] ==0:
    continue
    
  balls[x] -= 1
  balls[y] += 1
  if red[x]:
    red[y] = 1
  if balls[x]==0:
    red[x] = 0
print(sum(red))
  
  

