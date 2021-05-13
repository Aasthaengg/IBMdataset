#! python3
import math

def main():
    N = int(input())
    alist = [int(num) for num in input().split()]
    ans1 = 0
    ans2 = 0
    m = sum(alist) / N

    if sum(alist) % N == 0:
        ans = 0
        for i in range(N):
            ans += (alist[i] - m)**2
    else:
        mu = math.floor(m)
        mo = math.ceil(m)
        for i in range(N):
            ans1 += (alist[i] - mu)**2
            ans2 += (alist[i] - mo)**2

        if ans1 <= ans2:
            ans = ans1
        else:
            ans = ans2

    print(int(ans))


main()