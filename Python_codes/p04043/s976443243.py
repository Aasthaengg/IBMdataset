def actual(A, B, C):
    if (A, B, C) in [(5, 5, 7), (5, 7, 5), (7, 5, 5)]:
        return 'YES'

    return 'NO'

A, B, C = map(int, input().split())  
print(actual(A, B, C))