n,m=map(int,input().split())
xy = [list(map(int, input().split())) for _ in range(m)]
l=[1]*n
out_=[0]*n
in_=[0]*n
c=1

check=0
for i in range(m):
    if check==0:
        if xy[i][0]==1:
            in_[xy[i][1]-1]+=1
            check=1
        else:
            if xy[i][1]==1:
                in_[xy[i][1]-1]+=1
                check=1
        l[xy[i][0]-1]-=1
        l[xy[i][1]-1]+=1
    else:
        l[xy[i][0]-1]-=1
        l[xy[i][1]-1]+=1
        if l[xy[i][0]-1]==0 and in_[xy[i][0]-1]!=0:
            in_[xy[i][0]-1]=0
            in_[xy[i][1]-1]+=1
        elif l[xy[i][0]-1]!=0 and in_[xy[i][0]-1]!=0:
            in_[xy[i][1]-1]+=1
ans=0
for i in range(n):
    if in_[i]!=0:
        ans+=1
print(ans)