import collections
w = input()
w = sorted(w)

if len(w) % 2 != 0:
    print('No')
    exit()
C = collections.Counter(w)

C = list(C.values())


for i in range(len(C)):
    if C[i] % 2 != 0:
        print('No')
        exit()

print('Yes')
