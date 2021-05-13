def c_be_together():
    N = int(input())
    A = [int(i) for i in input().split()]
    a_ave = sum(A) // N
    return min(sum([(a - option)**2 for a in A]) for option in (a_ave, a_ave + 1))

print(c_be_together())