import sys
l=list(map(int, input().split()))
if 5 in l:
    l.remove(5)
    if 5 in l and 7 in l:
        print("YES")
        sys.exit()
print("NO")
