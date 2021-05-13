s = input()
if 'E' in s:
    if 'W' not in s:
        print('No')
        exit()
if 'E' not in s:
    if 'W' in s:
        print('No')
        exit()
if 'N' not in s:
    if 'S' in s:
        print('No')
        exit()
if 'N' in s:
    if 'S' not in s:
        print('No')
        exit()
print('Yes')