# AGC 001: A – BBQ Easy
N = int(input())
L = [int(s) for s in input().split()]
L.sort()

print(sum(L[::2]))