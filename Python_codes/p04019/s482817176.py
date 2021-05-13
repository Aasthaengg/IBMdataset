import sys
def input():
  return sys.stdin.readline().rstrip()

ma={"N":0,"S":0,"E":0,"W":0}

def func(S):
  for x in S:
    ma[x]=1
  if ma["N"]!=ma["S"]:
    return False
  if ma["W"]!=ma["E"]:
    return False
  return True

S=input()
print("Yes" if func(S) else "No")
