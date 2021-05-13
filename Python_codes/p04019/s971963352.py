S = input()
if S.count('N') > 0 and S.count('S') == 0 or S.count('N') == 0 and S.count('S') > 0 or S.count('W') > 0 and S.count('E') == 0 or S.count('W') == 0 and S.count('E') > 0:
    print('No')
else:
    print('Yes')
