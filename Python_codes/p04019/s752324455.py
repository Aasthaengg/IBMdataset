l = list(input())
l=set(l)

if len(l)==4: print('Yes')
elif len(l)==2 and 'N' in l and 'S' in l: print('Yes')
elif len(l)==2 and 'E' in l and 'W' in l: print('Yes')
else: print('No')