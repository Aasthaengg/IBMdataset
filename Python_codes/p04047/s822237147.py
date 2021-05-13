n = int(input())
l = sorted([int(i) for i in input().split()])

l2 = [min(l[i],l[i-1]) for i in range(1,2*n,2)]

print(sum(l2))
