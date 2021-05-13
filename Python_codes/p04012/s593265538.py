w = input()
char = [chr(ord('a') + i) for i in range(26)]
for c in char:
    if w.count(c) % 2 != 0:
        print('No')
        break
else:
    print('Yes')