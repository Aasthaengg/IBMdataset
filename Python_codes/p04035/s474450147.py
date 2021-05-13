def read_data():
    N, L = map(int, input().split())
    As = list(map(int, input().split()))
    return N, L, As

def solve(N, L, As):
    for i in range(N - 1):
        if As[i] + As[i + 1] >= L:
            return list(range(1, i + 1)) + list(range(N - 1, i, - 1))
    return []

N, L, As = read_data()
ans = solve(N, L, As)
if ans:
    print("Possible")
    for i in ans:
        print(i)
else:
    print("Impossible")
