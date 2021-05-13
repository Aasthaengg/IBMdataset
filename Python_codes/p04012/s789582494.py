s = input()

for i in set(s):
    if s.count(i) % 2 != 0:
        print('No')
        break
else:
    print('Yes')