n, *A = map(int, open(0).read().split())
m = round(sum(A) / n)
print(sum(map(lambda x: (x-m)**2, A)))