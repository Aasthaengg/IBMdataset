# -*- coding: utf-8 -*-

import io
import sys
import math
from decimal import Decimal, ROUND_HALF_UP


def format_multi_line_answer(lst):
    ans = ""
    ans += f"{len(lst)}\n"  # Line count
    for y in lst:
        ans += f"{y}\n"
    return ans

def solve(n,n_lst):
    # implement process
    
    #中央値を取り、四捨五入する
    target = Decimal(sum(n_lst)/n).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    cost = 0
    for a in n_lst:
        cost += pow(a-target,2)
    return cost

def main():
    # input
    n = int(input())
    n_lst = list(map(int, input().split()))

    # process
    ans = str( solve(n,n_lst ) )
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
4
-100 -100 -100 -100

"""
_EXPECTED = """\
8

"""

def logd(str):
    """usage:
    if _DEB: logd(f"{str}")
    """
    if _DEB: print(f"[deb] {str}")

### MAIN ###
if __name__ == "__main__":
    if _DEB:
        sys.stdin = io.StringIO(_INPUT)
        print("!! Debug Mode !!")

    ans = main()

    if _DEB:
        print()
        if _EXPECTED.strip() == ans.strip(): print("!! Success !!")
        else: print(f"!! Failed... !!\nANSWER:   {ans}\nExpected: {_EXPECTED}")