N=int(input());a=[int(i) for i in input().split()]
print(min([sum([(n-i)**2 for n in a])for i in range(-100,101)]))