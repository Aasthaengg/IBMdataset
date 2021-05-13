def resolve(n):
    def ans(n, a):
        if n == 0:
            return a
        else:
            a += n
            return ans(n-1,a)
    return ans(n, 0)

print(resolve(int(input())))