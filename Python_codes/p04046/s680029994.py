from sys import stdin
import sys
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7
input = stdin.readline

H, W, A, B = [int(x) for x in input().rstrip().split()]

factorial = [1]
for i in range(1, H+W):
	factorial.append(factorial[i-1] * i % mod)

def power(x, y):
	if y == 0:
		return 1
	elif y == 1:
		return x % mod
	elif y % 2 == 0:
		return power(x, int(y/2)) ** 2 % mod
	else:
		return power(x, int((y-1)/2)) ** 2 * x % mod
def C(n, r):
	return (((factorial[n] * x_inv[r]) % mod) * x_inv[n-r]) % mod
# x_inv = []
# for i in range(H+W):
# 	x_inv.append(power(factorial[i], mod-2))

x_inv = [0] * (H+W)
x_inv[-1] = power(factorial[-1], mod-2)
for i in range(H+W-2, -1, -1):
	x_inv[i] = x_inv[i+1] * (i+1) % mod

sum = 0
for i in range(B, W):
	sum += C(i+H-A-1, i) * C(A+W-i-2, A-1) % mod
print(sum%mod)
