import math
n = int(input())

cards = [0] * n

for i in range(n):
  cards[i] = int(input())

ans = 0


for i in range(n):
  ans += math.floor(cards[i] / 2)
  cards[i] = cards[i] % 2
  if cards[i] == 1 and not(i == (n - 1)) and not(cards[i + 1] == 0):
    ans += 1
    cards[i + 1] = cards[i + 1] - 1

print(ans)
