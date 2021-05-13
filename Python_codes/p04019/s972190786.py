s = input()

x = False
if 'N' in s and 'S' in s:
    x = True
if 'N' not in s and 'S' not in s:
    x = True
y = False
if 'W' in s and 'E' in s:
    y = True
if 'W' not in s and 'E' not in s:
    y = True

if x and y:
    print('Yes')
else:
    print('No') 