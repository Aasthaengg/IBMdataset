w = input()
for x in w:
    if w.count(x) % 2 != 0:
        print('No')
        exit()
print('Yes')