n = int(input())
S = []
for _ in range(n):
    S.append(int(input()))
ans=0
for i in range(len(S)):
    ans+= S[i] // 2

    if i==len(S)-1:
        break
    if S[i]%2 == 1 and S[i+1] >= 1:
        ans+=1
        S[i+1] -= 1
print(ans)