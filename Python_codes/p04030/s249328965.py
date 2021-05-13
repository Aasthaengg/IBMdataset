#!/usr/bin/env python3

def solve(s):
  l = []
  for c in s:
    if c == "0" or c == "1":
      l.append(str(c))
    elif len(l):
      l.pop()
  return "".join(l)




def main():
  s = input()
  print(solve(s))
  return

if __name__ == '__main__':
  main()
