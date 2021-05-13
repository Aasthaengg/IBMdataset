N, A = map(int, input().split())
x = [int(i) for i in input().split()]

x.sort()
x = [i - A for i in x]
D = {0 : 1}
for i in x :
    for j, k in list(D.items()) :
        D[i+j] = D.get(i+j, 0) + k

print(D[0] - 1)
