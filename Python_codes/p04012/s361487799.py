w = list(input())
x = list(set(w))
for i in x:
    y = w.count(i)
    if y % 2 != 0:
        print('No')
        exit(0)
print('Yes')