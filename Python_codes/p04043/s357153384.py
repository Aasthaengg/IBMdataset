import sys
a,b,c=map(int,input().split())

l=[a,b,c,a,b]
for x in range(3):
    if l[x]==l[x+1] and l[x]==5 and l[x+2]==7:
        print('YES')
        sys.exit()
print('NO')
