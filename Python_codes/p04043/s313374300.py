A, B, C = map(int, input().split())
S = [0]*3

S[0] = A
S[1] = B
S[2] = C

S.sort()

if(S[0]==5 and S[1]==5 and S[2]==7):
    print('YES')
else:
    print('NO')