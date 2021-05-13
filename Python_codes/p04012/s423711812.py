w = input()
for i in range(26):
    if w.count(chr(97+i)) % 2 == 1:
        print('No')
        exit()
print('Yes')
