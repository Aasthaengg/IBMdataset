import numpy as np

s = input()
ans = ['No', 'Yes']

judge = (('N' in s) == ('S' in s) and ('W' in s) == ('E' in s))
print(ans[judge])