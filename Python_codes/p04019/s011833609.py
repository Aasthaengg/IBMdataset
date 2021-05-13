S=list(set(input()))
if len(S)==4 or set(S)==set(['N','S']) or set(S)==set(['W','E']):
    print('Yes')
else:
    print('No')