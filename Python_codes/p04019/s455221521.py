import sys
s = input()
if 'N' in s:
    if 'S' not in s:
        print('No')
        sys.exit()
if 'W' in s:
    if 'E' not in s:
        print('No')
        sys.exit()
if 'E' in s:
    if 'W' not in s:
        print('No')
        sys.exit()
if 'S' in s:
    if 'N' not in s:
        print('No')
        sys.exit()
print('Yes')