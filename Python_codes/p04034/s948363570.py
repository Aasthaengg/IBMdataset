n,m = map(int,input().split())
kosu = [1 for _ in range(n)]
aka = [0 for _ in range(n)]
aka[0] += 1
for i in range(m):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  if aka[a]==1:
    #論理和
    aka[b] |= 1
    if kosu[a]<2:
      aka[a] -=1
  kosu[a] -=1
  kosu[b] += 1
 # print("kosu",kosu)
  #print("aka",aka)
print(aka.count(1))