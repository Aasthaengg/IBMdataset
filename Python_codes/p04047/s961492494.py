N = int(input())
L = list(map(int,input().split()))
L.sort()
Sum = 0
for i in range(0,N*2,2):
  Sum += L[i]
print(Sum)