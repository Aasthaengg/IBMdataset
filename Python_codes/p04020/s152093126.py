N = int(input())

first = int(input())
answer = first//2
before = first%2
for _ in range(N-1):
  A = int(input())
  answer += (A+before)//2
  before = (A+before)%2
  if A == 0:
    before = 0
print(answer)