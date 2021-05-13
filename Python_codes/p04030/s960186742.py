s = input()

ans = []

for c in s:
    if c != 'B':
        ans += c
    else:
        if len(ans) > 0:
            del ans[-1]
            
print(''.join(ans))