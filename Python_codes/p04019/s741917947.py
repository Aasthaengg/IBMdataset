import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=set(input())
    ans='No'
    if s=={'N','S','W','E'} or s=={'N','S'} or s=={'W','E'}:
        ans='Yes'
    print(ans)
resolve()