def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    cost = 10**10

    for a in range(-200, 201):
        c = 0
        for i in range(N):
            c += (a - A[i])**2
        if c < cost:
            cost = c
    print(cost)
if __name__ == "__main__":
    main()