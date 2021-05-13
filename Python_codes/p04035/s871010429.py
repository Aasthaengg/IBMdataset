N, L = map(int, input().split())
A = [int(a) for a in input().split()]

CanRemain = []
CutFirst = []
for i in range(N-1):
    if A[i] + A[i+1] >= L: CanRemain.append(i+1)
    else: CutFirst.append(i+1)

if not CanRemain: print("Impossible")
else:
    print("Possible")
    for num in CutFirst:
        if num < CanRemain[-1]: print(num)
        else: break
    for i in reversed(range(len(CutFirst))):
        if CutFirst[i] > CanRemain[-1]: print(CutFirst[i])
        else: break
    for num in CanRemain: print(num)