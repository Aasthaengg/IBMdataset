n, m = map(int, input().split())
prob = [False] * (n + 1)
exact = [False] * (n + 1)
prob[1] = exact[1] = True
num_in = [1] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    if num_in[x] == 1 and exact[x]:
        exact[y] = True
        exact[x] = False
        prob[x] = False
        prob[y] = True
    elif num_in[x] > 1 and exact[x]:
        exact[x] = False
        prob[y] = True
    elif prob[x]:
        if num_in[x] == 1:
            prob[x] = False
        prob[y] = True
    num_in[y] += 1
    num_in[x] -= 1
print(prob.count(True))