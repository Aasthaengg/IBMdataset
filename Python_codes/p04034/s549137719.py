import sys,math,collections,itertools
input = sys.stdin.readline

N,M=list(map(int,input().split()))
ball = [0]*(N+1)
ball[1]=1
ball_num = [1]*(N+1)
for i in range(M):
    x,y=map(int,input().split())
    if ball[x]==1:
        ball[y]=1
    ball_num[x]-=1
    ball_num[y]+=1
    if ball_num[x]==0:
        ball[x]=0
    
cnt = 0
for a,b in zip(ball_num,ball):
    cnt += (a!=0 and b != 0)
print(cnt)