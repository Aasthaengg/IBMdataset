def main3():
    N, M = map(int, input().split())

    ball  = [0, 1] + [1 for i in range(N - 1)]
    rflag = [0, 1] + [0 for i in range(N - 1)] 

    for i in range(M):
        x, y = map(int, input().split())

        if rflag[x] == 1:
            rflag[y] = 1

        ball[x] -= 1
        ball[y] += 1

        if ball[x] == 0:
            rflag[x] = 0

    ans = sum(rflag[1:])
    print(ans)
    
if __name__ == "__main__":
    main3()