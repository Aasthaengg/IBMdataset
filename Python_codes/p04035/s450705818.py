N, L = map(int, input().split())
a = list((map(int, input().split())))
longest = 0
longest_i = N
for i in range(N-1):
    knot = a[i]+a[i+1]
    if knot > longest:
        longest = knot
        longest_i = i+1
if longest < L:
    print("Impossible")
else:
    print("Possible")
    for i in range(1,longest_i):
        print(i)
    for j in range(N-1,longest_i-1,-1):
        print(j)
