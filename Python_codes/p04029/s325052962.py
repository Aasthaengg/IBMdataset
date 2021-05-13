# 043_a
N = int(input())
if 1 <= N & N <= 100:
    result = 0
    for i in range(N):
        count = N - i
        result += count
        if count == 1:
            print(result)