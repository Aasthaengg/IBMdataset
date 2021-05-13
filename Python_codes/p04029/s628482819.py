N = int(input())

if N % 2 == 0:
    result = (N / 2) * (1 + N)
else:
    result = ((N - 1) / 2) * N + N

print(int(result))