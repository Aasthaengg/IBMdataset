N = int(input())
L = [int(x) for x in input().split()]
L.sort(reverse=True)
print(sum(L[1::2]))