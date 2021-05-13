N = int(input())
L = [int(x) for x in input().split()]
L.sort()
answer = sum(L[::2])
print(answer)