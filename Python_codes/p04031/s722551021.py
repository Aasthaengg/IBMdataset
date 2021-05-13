n = int(input())
a = [int(i) for i in input().split()]

m = sum(a) / len(a)
num = round(m)

loss = 0
for n in a:
	loss += (n - num)**2

print(loss)
