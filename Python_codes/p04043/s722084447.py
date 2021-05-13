A, B, C = map(int, input().split())
num = [0]*11
num[A] += 1
num[B] += 1
num[C] += 1
ans = 'YES' if num[5] == 2 and num[7] == 1 else 'NO'
print(ans)