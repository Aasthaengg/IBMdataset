from itertools import*
_, *a = map(int, open(0))
print(sum(sum(l)//2 for _, l in groupby(a, key=lambda x:x>0)))