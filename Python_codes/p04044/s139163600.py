# -*- coding: utf-8 -*-

import io
import sys
import math

def format_multi_line_answer(lst):
    ans = ""
    ans += f"{len(lst)}\n"  # Line count
    for y in lst:
        ans += f"{y}\n"
    return ans

def solve():
    # implement process
    pass

def main():
    # input
    n,l = map(int, input().split())
    a_lst = sys.stdin.read().split()
        
    # process
    a_lst.sort()
    ans = "".join(a_lst)
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
3 3
dxx
axx
cxx
"""


_EXPECTED = """\
axxcxxdxx
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