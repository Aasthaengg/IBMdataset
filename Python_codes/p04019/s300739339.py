*S, = input()

flag_x = False
flag_y = False

if 'S' in S and 'N' in S:
    flag_y = True
if 'S' not in S and 'N' not in S:
    flag_y = True

if 'E' in S and 'W' in S:
    flag_x = True
if 'E' not in S and 'W' not in S:
    flag_x = True

if flag_x and flag_y:
    print('Yes')
else:
    print('No')