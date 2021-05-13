s = input()
if 'N' in s and 'S' not in s:
    print('No')
elif 'S' in s and 'N' not in s:
    print('No')
elif 'W' in s and 'E' not in s:
    print('No')
elif 'E' in s and 'W' not in s:
    print('No')
else:
    print('Yes')