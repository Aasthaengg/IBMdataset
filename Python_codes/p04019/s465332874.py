s=input()
res = ''
if 'N' in s:
    if 'S' not in s:
        res = 'No'
if 'S' in s:
    if 'N' not in s:
        res = 'No'
if 'E' in s:
    if 'W' not in s:
        res = 'No'
if 'W' in s:
    if 'E' not in s:
        res = 'No'
if res == '':
    print('Yes')
else:
    print(res)

