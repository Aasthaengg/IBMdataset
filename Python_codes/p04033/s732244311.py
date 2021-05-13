'''
Created on 2020/08/19

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  a,b=map(int,pin().split())
  if a<0 and b<0:
    if (abs(b-a)+1)%2==0:
      print("Positive")
    else:
      print("Negative")
  elif a>0 and b>0:
    print("Positive")
  else :
    print("Zero")
  return

main()
