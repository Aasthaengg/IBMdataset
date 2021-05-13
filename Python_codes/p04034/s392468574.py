def main():
    n, m = list(map(int, input().split()))
    ans = set([1, ])
    balls = [1] * n
    for _ in range(m):
        x, y = list(map(int, input().split()))
        if x in ans:
            ans.add(y)
        if balls[x - 1] == 1 and x in ans:
            ans.remove(x)
        balls[x - 1] -= 1
        balls[y - 1] += 1
    print(len(ans))

if __name__ == '__main__':
    main()
