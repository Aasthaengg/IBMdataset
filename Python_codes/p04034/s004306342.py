def main():
    N,M  = map(int,(input().split()))
    BOX = [0]+[1]*N
    RED = [False]*(N+1)
    RED[1] = True

    for _ in range(M):
        x,y = map(int,(input().split()))
        BOX[x] -=1
        BOX[y] +=1
        if RED[x]:
            RED[y]=True
        if BOX[x]==0:
            RED[x]=False
    cnt = 0
    for r in RED:
        if r:
            cnt +=1
    print(cnt)



if __name__ == '__main__':
    main()
