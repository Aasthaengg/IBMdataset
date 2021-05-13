s = input()
li = [[1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]]

direction = [0] * 4

for i in s:
    if i == 'N':
        direction[0] = 1
    elif i == 'S':
        direction[1] = 1
    elif i == 'W':
        direction[2] = 1
    else:
        direction[3] = 1

if direction in li:
    print('Yes')
else:
    print('No')