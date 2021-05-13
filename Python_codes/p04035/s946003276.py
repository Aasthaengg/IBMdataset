#gcdは3.4.3だとfractionsにある
from fractions import gcd
import math

from math import factorial as f

from math import ceil,floor,sqrt


import bisect
import re
import heapq


from copy import deepcopy
import itertools

from sys import exit

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

yes = "Yes"
no = "No"




def main():
    a,b,c = mi()
    if c-a-b<=0:
        print(no)
        exit()
    else:
        if (c-a-b)**2 > 4*a*b:
            print(yes)#gcdは3.4.3だとfractionsにある
from fractions import gcd
import math

from math import factorial as f

from math import ceil,floor,sqrt


import bisect
import re
import heapq


from copy import deepcopy
import itertools

from sys import exit

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

yes = "YES"
no = "NO"


def main():
    n,l = mi()
    a = li()

    flag = False
    lp = 0
    for i in range(n-1):
        if a[i]+a[i+1] >= l:
            print("Possible")
            flag = True
            lp = i+1
            break
    
    if not flag:
        print("Impossible")
        exit()

    for i in range(1,lp):
        print(i)
    for i in range(n-1,lp,-1):
        print(i)
    print(lp)
    
    

    


main()

