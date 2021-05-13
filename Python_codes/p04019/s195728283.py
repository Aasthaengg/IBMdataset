import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=set(input())
    ans='No'
    if s==set('NSWE') or s==set('NS') or s==set('WE'):
        ans='Yes'
    print(ans)
resolve()