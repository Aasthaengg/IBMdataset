N, L = map(int, input().split())
As = list(map(int, input().split()))

for iKnot in range(1, N):
    if As[iKnot - 1] + As[iKnot] >= L:
        print('Possible')
        for i in range(1, iKnot):
            print(i)
        for i in reversed(range(iKnot + 1, N)):
            print(i)
        print(iKnot)
        break
else:
    print('Impossible')
