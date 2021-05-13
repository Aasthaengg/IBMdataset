N,M=map(int,input().split())
balls=[1 for _ in range(N)]
answers=[0 for _ in range(N)]
answers[0]=1
for _ in range(M):
    x,y=map(int,input().split())
    balls[x-1]-=1
    balls[y-1]+=1
    if balls[x-1]>=1 and answers[x-1]==1:
        answers[y-1]=1
    elif balls[x-1]==0 and answers[x-1]==1:
        answers[x-1]=0
        answers[y-1]=1
print(sum(answers))
