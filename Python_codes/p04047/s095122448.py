n = int(input())
l = input().split()
int_l = []

for i in range(2*n):
	int_l.append(int(l[i]))

int_l.sort(reverse=True)

sum = 0

for i in range(n):
	sum += min(int_l[2*i],int_l[2*i+1])

print(sum)