w = [w for w in input()]
w1 = sorted(w)
w2 = sorted(w1[::2]*2)
print('Yes' if w1 == w2 else 'No')