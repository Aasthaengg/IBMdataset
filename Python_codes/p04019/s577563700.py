s=input()
s=set(s)
if s=={"N","E","S","W"} or s=={"N","S"} or s=={"E","W"}:
    print('Yes')
else:
    print('No')
