line = input().split(" ")
a = int(line[0])
b = int(line[1])

if a > 0:
  print("Positive")
elif a <= 0 and b >= 0:
  print("Zero")
else:
  c = b - a + 1
  if c % 2 == 0:
    print("Positive")
  else:
    print("Negative")