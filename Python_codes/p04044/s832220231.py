def solve():
  N, L = map(int, input().split())
  S = [input() for _ in range(N)]
  S.sort()
  ans = ''.join(S)
  return ans
print(solve())