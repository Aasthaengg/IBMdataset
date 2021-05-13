w = list(input())

for c in range(ord('a'), ord('z')+1):
    if w.count(chr(c)) % 2 == 1:
        print('No')
        break
else:
    print('Yes')