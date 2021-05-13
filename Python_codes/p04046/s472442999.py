import math

def modinv(a,m):
	b = m
	u = 1
	v = 0
	while(b):
		t = a // b
		a -= t * b
		a,b = b,a
		u -= t * v
		u,v = v,u
	u %= m
	if u < 0:
		u += m
	return u

inp = input().split(' ')
inpint = [int(i) for i in inp]
h = inpint[0]
w = inpint[1]
a = inpint[2]
b = inpint[3]

xfac = [0 for r in range(h+w-2)]
xfac_inv = [0 for r in range(h+w-2)]

for i in range(h+w-2):
	if i == 0:
		xfac[i] = 1
	else:
		xfac[i] = (xfac[i-1]*i)%1000000007

for i in reversed(range(h+w-2)):
	if i == h+w-3:
		xfac_inv[i] = modinv(math.factorial(i),1000000007)
	else:
		xfac_inv[i] = xfac_inv[i+1] * (i+1) % 1000000007

# print(xfac)
# print(xfac_inv)

# for i in range(h+w-2):
# 	print(xfac[i]*xfac_inv[i]%1000000007)

def com(a,b):
	return (xfac[a] * xfac_inv[b] * xfac_inv[a-b])%1000000007

sum = 0
for i in range(b,w):
	sum += com(i + h-a-1,h-a-1) * com((a-1)+w-i-1, w-i-1)
	sum %= 1000000007

print(sum)