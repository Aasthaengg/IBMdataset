#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n = int(input())
  la = [int(input()) for _ in range(n)]
  cnt = 0
  for i in range(n):
    cnt += (la[i]//2)
    la[i] -= 2*(la[i]//2)
    if i < n-1:
      n_pair = min(la[i], la[i+1])
      cnt += n_pair
      la[i] -= n_pair
      la[i+1] -= n_pair
  print(cnt)
  
if __name__=='__main__':
  main()

