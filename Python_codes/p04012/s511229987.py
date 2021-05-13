from collections import defaultdict as dd
def beautiful(s):
    D = dd(lambda:0)
    for c in s:
        D[c] += 1
    if any(d&1 for d in D.values()):
        return False
    else:
        return True

print('Yes' if beautiful(input()) else 'No') 
