def solve(a, b):
    if a <= 0 and 0 <= b:
        return 'Zero'
    if 0 < a:
        return 'Positive'
    length = b - a + 1
    return 'Positive' if length % 2 == 0 else 'Negative'


a, b = map(int, input().split())
print(solve(a, b))
