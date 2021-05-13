MOD = 10 ** 9 + 7
INF = 10 ** 11
import sys
sys.setrecursionlimit(100000000)

def main():
    N,M = map(int,input().split())
    possible = [0] * N
    possible[0] = 1
    ball_cnt = [1] * N
    for _ in range(M):
        x,y = map(int,input().split())
        x -= 1
        y -= 1
        if possible[x]:
            possible[y] = 1
            if ball_cnt[x] == 1:
                possible[x] = 0
        ball_cnt[x] -= 1
        ball_cnt[y] += 1
    ans = sum((b > 0)*p for b,p in zip(ball_cnt,possible))
    print(ans)
if __name__ == '__main__':
    main()
