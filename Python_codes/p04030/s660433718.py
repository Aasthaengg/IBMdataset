S = list(input())
ans = []

for i in range(len(S)):
    if(S[i] != 'B'):
        ans.append(S[i])
    elif(S[i] == 'B' and len(ans) != 0):
        ans.pop()

        
print(''.join(ans))