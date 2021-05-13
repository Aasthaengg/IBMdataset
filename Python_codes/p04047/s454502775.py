N = input()
L = [int(j) for j in input().split(' ')]
L.sort()
print(sum([L[j] for j in range(len(L)) if j % 2 == 0]))
