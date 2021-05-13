n, a = map(int, input().split())
x_i = map(int, input().split())
list = list(i - a for i in x_i)
anslist = [[0 for i in range(5001)] for j in range(n + 1)]
anslist[0][2500] += 1
anslist[1][2500] += 1
anslist[1][list[0] + 2500] += 1
for id in range(n + 1):
    if id == 0 or id == 1: continue
    num = list[id - 1]
    for x in range(5001):
        anslist[id][x] += anslist[id - 1][x]
        if 0 <= x - num < 5001:
            anslist[id][x] += anslist[id - 1][x - num]
print(anslist[n][2500] - 1)