N = int(input())
L = list(map(int, input().split()))
 
L_s = sorted(L)
A = sum(L_s[0::2])
 
print(A)