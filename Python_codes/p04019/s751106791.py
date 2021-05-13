import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    ans='No'
    if 'N' in s and 'S' in s and 'W' in s and 'E' in s:
        ans='Yes'
    elif 'N' in s and 'S' in s and \
            'W' not in s and 'E' not in s:
        ans='Yes'
    elif 'N' not in s and 'S' not in s and\
            'W' in s and 'E' in s:
        ans='Yes'
    print(ans)
resolve()