n = int(input())
l = [int(i) for i in input().split()]

val = float("inf")
for i in range(-100,101):
	new = 0
	for j in l:
		new += (i-j)**2	
	val = min(val,new)		
print(val)	
