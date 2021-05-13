#import numpy as np
#import functools
#import operator
#from itertools import combinations as comb
#from itertools import combinations_with_replacement as comb_with
#from itertools import permutations as perm


#N = int(input())
a,b= map(int,input().split())
#A = list(map(int,input().split()))
#B = list(map(int,input().split()))
#S= str(input())
#prod = functools.partial(functools.reduce, operator.mul)
#c=np.array(A)
#p=np.prod(A)

if a<0:
    if 0<=b:
        print('Zero')

    else:
        if abs(a-b)%2==0:
            print('Negative')
        else:
            print('Positive')
elif a==0:
    print('Zero')

else:
    print('Positive')
