N = int(input())

A = []

for i in range (0,N):
	A.append(int(input()))

temp = 0
total = 0

import math

for i in range (0, N):
	if A[i] != 0:
		temp+=A[i]
	else:
		total+=math.floor(temp/2)
		temp=0
        
total+=math.floor(temp/2)     

print(total)