def compare_strings(s1, s2):
    if s1 < s2:
        return True
    return False

n, l = map(int, input().split())
strings = [input() for i in range(n)]

print(''.join(sorted(strings)))
