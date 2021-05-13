input()
L=[int(l) for l in input().split()]
L.sort(reverse=True)
print(sum(L[1::2]))