# A - Range Product
import numpy as np

ans = ['Positive', 'Negative']

a, b = map(int, input().split())
if a<=0 & 0<=b:
    print('Zero')
else:
    sgn = max(-b,0) - max(-a-1,0)
    print(ans[sgn%2])