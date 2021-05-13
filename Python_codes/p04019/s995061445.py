S = input()

S_set = set(S)
if len(S_set) % 2 == 0:
    if S_set == set() or S_set == set(['N', 'S']) or S_set == set(['E', 'W']) or S_set == set(['N', 'S', 'E', 'W']):
        print('Yes')
    else:
        print('No')
else:
    print('No')