n, a = map(int, input().split())
x = list(map(int, input().split()))

x.sort()
x = [i - a for i in x]
# print(x)
D = {0 : 1}
for i in x:
    for j, k in list(D.items()):
        D[i+j] = D.get(i+j, 0) + k

    # print(D)
print(D[0] - 1)
