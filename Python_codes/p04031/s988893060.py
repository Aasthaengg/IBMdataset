def resolve():
    N = int(input())
    a_list = list(map(int, input().split()))
    if len(set(a_list)) == 1:
        print(0)
    else:
        # コストは最大でも10**6
        min_cost = 10 ** 6 + 1
        for x in range(-100, 101):
            cost = sum([(a -x)**2 for a in a_list])
            if cost < min_cost:
                min_cost = cost
        print(min_cost)

resolve()