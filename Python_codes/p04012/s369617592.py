w=input()
a=list('abcdefghijklmnopqrstuvwxyz')
for A in a:
    if w.count(A) % 2 == 1:
        print('No')
        exit()
print('Yes')