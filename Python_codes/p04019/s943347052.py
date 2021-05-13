from collections import Counter
s = input()
C = Counter(s)
if len(C) % 2 != 0:
    print('No')
    exit()
else:
    if len(s) == 4:
        print('Yes')
    else:
        if 'N' in s and 'S' in s:
            print('Yes')
        elif 'E' in s and 'W' in s:
            print('Yes')
        else:
            print('No')