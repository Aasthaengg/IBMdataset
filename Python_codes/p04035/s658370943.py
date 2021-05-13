N, L = map(int, input().split())
a = list(map(int, input().split()))
max_value = max_value_index = 0
for index, i in enumerate(zip(a[:-1], a[1:])):
    if max_value < sum(i):
        max_value = sum(i)
        max_value_index = index

print("Possible\n" + "\n".join([str(i) for i in range(1, max_value_index + 1)] + [str(i) for i in range(N - 1, max_value_index, -1)]) if max_value >= L else "Impossible")