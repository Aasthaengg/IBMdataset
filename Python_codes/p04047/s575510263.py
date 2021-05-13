n=int(input())
a=[int(i) for i in input().split()]
a.sort()
print(sum([a[i] for i in range(0,2*n,2)]))