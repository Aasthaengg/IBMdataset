S=input()
hasN = S.find('N') >= 0
hasS = S.find('S') >= 0
hasE = S.find('E') >= 0
hasW = S.find('W') >= 0
if (hasN and hasS or not hasN and not hasS) and (hasE and hasW or not hasE and not hasW):
    print('Yes')
else:
    print('No')