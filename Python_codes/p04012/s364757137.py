from collections import Counter
cnt=Counter(input())
print('No' if any([x&1 for x in cnt.values()]) else 'Yes')