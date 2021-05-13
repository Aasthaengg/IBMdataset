N = int(input())
L = sorted([int(i) for i in input().split()])

print(sum(L[::2]))
