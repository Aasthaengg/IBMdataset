a, b = map(int, input().split())


def is_neg(num):
    return num < 0


if a == 0 or b == 0:
    print("Zero")
    exit()

if is_neg(a) and not is_neg(b):
    print("Zero")
    exit()


neg_count = 0
if is_neg(a):
    neg_count += abs(a)

if is_neg(b):
    neg_count -= abs(b) - 1

if neg_count % 2:
    print("Negative")
else:
    print("Positive")
