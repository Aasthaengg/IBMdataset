# 2n = n * 2 pairs optimal greedy contradiction 1 is paired with k 2 is with j if we move 1 to 2 and k to j
def main():
    n = int(input())

    arr = [int(x) for x in input().split(" ")]

    arr.sort()

    ans = 0

    for i in range(2*n):

        if (i % 2) == 0:
            ans += arr[i]

    print(ans)

main()
