import numpy as np
a,b = map(int,input().split(' '))
if np.sign(a)==1 and np.sign(b) == 1:
    print('Positive')
elif np.sign(a) == -1 and np.sign(b) == 1:
    print('Zero')
elif np.sign(a) == -1 and np.sign(b) == -1:
    if (b - a + 1) % 2 == 0:
        print('Positive')
    else:
        print('Negative')