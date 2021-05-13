s = input()
for i in set(s):
    if not s.count(i) % 2 == 0:
        print('No')
        exit()

print('Yes')
