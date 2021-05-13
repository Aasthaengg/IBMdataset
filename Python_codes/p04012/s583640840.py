from collections import Counter

s = list(input())

l = list(Counter(s).values())
for i in range(len(l)):
    if l[i] % 2 == 1:
        print('No')
        exit()
print('Yes')
