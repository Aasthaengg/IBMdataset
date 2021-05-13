N = int(input())
A = [int(input()) for _ in range(N)]


def counter(ar):
    count = 0
    for i in range(N):
        # print(i, ar, count)
        if i > 0:
            c = min(ar[i - 1], ar[i])
            ar[i - 1] -= c
            ar[i] -= c
            count += c
        c = ar[i] // 2
        ar[i] -= c * 2
        count += c
        if i < N - 1:
            c = min(ar[i], ar[i + 1])
            ar[i] -= c
            ar[i + 1] -= c
            count += c
    return count

# print(N)
# print(A)

# greedy left -> right, left <- right, take max
AA1 = A[:]
c1 = counter(AA1)
AA2 = A[::-1]
c2 = counter(AA2)
# print(c1)
# print(c2)
print(max(c1, c2))