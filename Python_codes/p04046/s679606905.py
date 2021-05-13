H, W, A, B = map(int,input().split())
P = 10**9+7
# H, W, A, B = map(int,"2 3 1 1".split())

M = H+W-1
factlist = [1] * (H+W)
factinvlist = [1] * (H+W)
t = 1
for i in range(M):
	t = (t * (i+1)) % P
	factlist[i+1] = t
t = pow(factlist[M],P-2,P)
factinvlist[M] = t
for i in range(M):
	t = (t * (M-i)) % P
	factinvlist[M-i-1] = t

def comb(i,j):
	return (factlist[i+j] * factinvlist[i] * factinvlist[j]) % P

s = 0
i = 0
while H-A-i-1 >= 0 and B+i <= W and A+i <= H and W-B-i-1 >= 0:
#	print((H-A-i,B+i+1))
	s = (s + comb(H-A-i-1,B+i) * comb(A+i,W-B-i-1)) % P
	i += 1	
print(s)

