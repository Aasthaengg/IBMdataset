_, _, *s = open(0).read().split()
print(''.join(sorted(s)))