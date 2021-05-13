s = input()
if (s.count('N')>0)^(s.count('S')>0) or (s.count('E')>0)^(s.count('W')>0):
    print('No')
else:
    print('Yes')