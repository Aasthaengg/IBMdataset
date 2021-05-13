a, b = map(int, input().split())

def f(a, b):
    if a <= 0 <= b:
        return 0
    if a > 0:
        return 1
    b = min(b, -1)
    n = b - a + 1
    return (-1) ** n

words = ['Zero', 'Positive', 'Negative']
print(words[f(a, b)])
