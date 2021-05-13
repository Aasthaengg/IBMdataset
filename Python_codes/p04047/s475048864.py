def resolve():
    N = int(input())
    L = list(reversed(sorted([int(i) for i in input().split()])))
    sumA = 0
    for l in L[1::2]:
        sumA += l
    print(sumA)


resolve()
