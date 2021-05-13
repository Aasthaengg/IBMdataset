A = [i for i in input().split()]

A.sort()
s = "".join(A)

YN = lambda b: print('YES') if b else print('NO')
YN( s == "557" )

