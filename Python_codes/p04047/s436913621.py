N=int(input()) 
L = sorted([int(i) for i in input().split()], key=lambda x: x)

foodCount = 0
for i in range(0,len(L), 2):
   foodCount += min(L[i], L[i+1])

print(foodCount)
