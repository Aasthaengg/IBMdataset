import numpy as np

def transfer(state, x, y):
    state[x][0] -= 1
    state[y][0] += 1
    if state[x][0] == 0:
        if state[x][1] == 1:
            state[x][1] = 0
            state[y][1] = 1
    else:
        if state[x][1] == 1:
            state[y][1] = 1
            
n, m = map(int, input().split())

state = [[1, 0] for _ in range(n)]
state[0][1] = 1
for i in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    transfer(state, x, y)

print(np.sum(state, axis=0)[1])