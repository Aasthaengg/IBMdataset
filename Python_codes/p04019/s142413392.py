s = input()

angle = {'N':0, 'W':0, 'S':0, 'E':0}

for i in s:
    angle[i] += 1


if angle['N'] > 0 and angle['S'] == 0:
    print('No')
    exit()

if angle['S'] > 0 and angle['N'] == 0:
    print('No')
    exit()

if angle['W'] > 0 and angle['E'] == 0:
    print('No')
    exit()

if angle['E'] > 0 and angle['W'] == 0:
    print('No')
    exit()

print('Yes')