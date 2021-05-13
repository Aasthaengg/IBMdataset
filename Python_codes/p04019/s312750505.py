s = input()

d = [c in s for c in 'NSEW']
if d[0] == d[1] and d[2] == d[3]:
    print('Yes')
else:
    print('No')