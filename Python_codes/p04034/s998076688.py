def solve():
    ans = 0
    N, M = map(int, input().split())
    lis = [1]*N
    lis[0] = -1 #赤が入っている可能性があればマイナス
    for _ in range(M):
        x,y = map(int, input().split())
        x -= 1
        y -= 1
        if lis[x]<0:
            lis[y] = -(abs(lis[y])+1)
            lis[x] += 1
        else:
            if lis[y]==0:
                lis[y] = 1
            else:
                lis[y] = (abs(lis[y])+1)*lis[y]//abs(lis[y])
            lis[x] -= 1
    ans = sum(map(lambda x:x<0,lis))
    return ans
print(solve())