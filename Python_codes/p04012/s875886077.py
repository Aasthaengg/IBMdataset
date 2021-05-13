s = input()
from collections import Counter
print('Yes' if all([cnt%2==0 for cnt in Counter(s).values()]) else 'No')
