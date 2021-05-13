import sys

input = sys.stdin.readline
MOD = 1000000007

S = input()[:-1]

x = [0,0,0,0]

for i in range(len(S)):
    if S[i] == 'N':
        x[0]+=1
    if S[i] == 'S':
        x[1]+=1
    if S[i] == 'E':
        x[2]+=1
    if S[i] == 'W':
        x[3]+=1


if x.count(0) == 0:
    print("Yes")
    exit()
else:
    if x[:2].count(0) == 0 and x[2:].count(0) == 2:
        print("Yes")
        exit()
    if x[:2].count(0) == 2 and x[2:].count(0) == 0:
        print("Yes")
        exit()
    
print("No")