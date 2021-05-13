import sys
input = sys.stdin.readline

# B - Box and Ball
N, M = map(int, input().split())

boxes = [1] * (N + 1)
boxes[0] = 0

ball_exists = set()
ball_exists.add(1)

for i in range(M):
  x, y = map(int, input().split())

  boxes[x] -= 1
  boxes[y] += 1
  
  if x in ball_exists:
    if boxes[x] == 0:
      ball_exists.remove(x)

      if len(ball_exists) == 1 and y in ball_exists:
        ball_exists.clear()

    ball_exists.add(y)

  #print(boxes)
  #print(ball_exists)

print(len(ball_exists))