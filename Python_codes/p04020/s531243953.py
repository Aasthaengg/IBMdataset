N = int(input())
 
tmp = int(input())
rlt = tmp//2
tmp -= 2*(tmp//2)

for i in range(1,N):
  a = int(input())
  if a == 0:
    tmp = 0
  elif tmp == 1:
    rlt += 1
    a -= 1
  tmp = a
  rlt += tmp//2
  tmp -= 2*(tmp//2)
  
print(rlt)