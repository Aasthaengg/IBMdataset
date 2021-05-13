#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

# @njit
def solve(n,m,queries):
  redInBox   = [False] * (n+1)
  amountOfBalls = [1] * (n+1)
  redInBox[1] = True
  
  for query in queries:
    x,y = query
    if redInBox[x]:
      redInBox[y] = True
      amountOfBalls[x] -= 1
      amountOfBalls[y] += 1
      if amountOfBalls[x] == 0:
        redInBox[x] = False
    else:
      amountOfBalls[x] -= 1
      amountOfBalls[y] += 1
 
  return sum(redInBox)



def main():
  N,M = map(int,input().split())
  queries = [list(map(int,input().split())) for _ in range(M)]
  print(solve(N,M,queries))
  return

if __name__ == '__main__':
  main()
