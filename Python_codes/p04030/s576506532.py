s = input()
t = []
r = 0

for i in range(len(s)):
    if s[i] == '0':
        t.append('0')
        r += 1
    elif s[i] == '1':
        t.append('1')
        r += 1    
    else:
        if r != 0:
            t.pop(r-1)
            r -= 1

print(''.join(t))