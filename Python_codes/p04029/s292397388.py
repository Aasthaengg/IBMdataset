"""
in1 = ''
"""
in1 = input()

N = int(in1)
RC = 0

for idx1 in range(N):
    RC = RC + idx1 + 1

print(RC)
