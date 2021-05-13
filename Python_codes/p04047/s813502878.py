N = [int(v) for v in input().split()]
L = [int(v) for v in input().split()]
L.sort()
L_even=L[0::2]
goukei=sum(L_even)
print(str(goukei))
