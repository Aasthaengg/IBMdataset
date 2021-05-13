url = "https://atcoder.jp/contests/abc043/tasks/abc043_a"

def main():

    a = int(input())
    ans = 0
    for i in range(1, a + 1):
        ans += i
    print(ans)

if __name__ == '__main__':
    main()


