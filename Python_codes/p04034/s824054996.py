import numpy as np
n, m = map(int, input().split())
'''
xx = []
yy = []
'''
box = np.zeros((n, 2))
box[:, 0] = 1
box[0, 1] = 1


count = 0
for _ in range(m):
    x, y = map(int, input().split())
    '''
    xx.append(x)
    yy.append(y)
    '''
    if (box[x - 1, 1] == 1):
        box[y - 1, 1] = 1

    box[x - 1, 0] -= 1

    if (box[x - 1, 0] == 0):
        box[x - 1, 1] = 0

    box[y - 1, 0] += 1

    # 赤玉が一度でもある場合
tar = box[:, 1]
ans = np.sum(tar != 0)
print(ans)

#xy = [list(map(int, input().split())) for _ in range(m)]
