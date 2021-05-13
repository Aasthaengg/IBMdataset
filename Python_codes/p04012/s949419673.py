# -*- coding: utf-8 -*-
# template: v1.2

import io
import sys
import math

CASES = "abcdefghijklmnopqrstuvwxyz"

def solve(s):
    # implement process
    for c in CASES:
        if s.count(c) % 2 != 0:
            return "No"
    return "Yes"

def main():
    # input
    s = input()
    
    # process
    ans = str( solve(s) )
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
abaccaba
"""
_EXPECTED = """\
Yes

"""

def logd(str):
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