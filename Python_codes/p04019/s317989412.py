S = list(sorted(set(input())))
print('Yes' if S == ['E', 'N', 'S', 'W'] or S == ['E', 'W'] or S == ['N', 'S'] else 'No')