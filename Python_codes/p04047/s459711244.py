N = int(input())
L = list(map(int, input().split()))
L = sorted(L, reverse=True)
mL = L[1::2]
print(sum(mL))