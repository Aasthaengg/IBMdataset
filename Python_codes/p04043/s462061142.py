import sys
input = sys.stdin.readline

a,b,c = sorted(list(map(int,input().split())))
print('YES' if a==b and b==5 and c==7 else 'NO')
