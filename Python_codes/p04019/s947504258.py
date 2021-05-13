s = set(list(input()))
if any(s==set(list(cand)) for cand in ['NS','EW','NEWS']):
    print('Yes')
else:
    print('No')
