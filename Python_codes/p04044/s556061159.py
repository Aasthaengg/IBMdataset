n,k=map(int,input().split())
w=[]
for i in range(n):
  w.append(input())
w.sort()
print(''.join(w))
