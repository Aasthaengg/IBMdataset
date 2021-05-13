S = list(input())
S_after = []
for i in S:
    if i == '1':
        S_after.append('1')
    elif i == '0':
        S_after.append('0')
    elif i == 'B':
        if S_after == []:
            pass
        else:
            S_after.pop()
print(''.join(S_after))