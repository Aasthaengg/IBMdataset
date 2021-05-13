s = input()
x = 0
y = 0
s = list(set(s))
for i in range(len(s)):
    if s[i] == 'N':
        y += 1
    elif s[i] == 'W':
        x -= 1
    elif s[i] == 'S':
        y -= 1
    else:
        x += 1
print('Yes' if x == 0 and y == 0 else 'No')
