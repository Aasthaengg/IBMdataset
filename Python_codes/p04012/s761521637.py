w=input()
dp=[0]*200
for i in range(len(w)):
  dp[ord(w[i])]+=1
for i in range(200):
  if dp[i]%2!=0:
    print('No')
    exit()
print('Yes')