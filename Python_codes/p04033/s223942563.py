a, b = map(int, input().split())

a_pulus = a >= 0
b_pulus = b >= 0
a_minus = a < 0
b_minus = b < 0

if a_pulus & b_pulus:
    print("Positive")
elif a_minus & b_pulus:
    print("Zero")
else:
    if (b - a + 1) % 2 == 0:
        print("Positive")
    else:
        print("Negative")
