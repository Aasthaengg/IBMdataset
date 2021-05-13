'''
Created on 2020/08/19

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  S=pin()[:-1]
  T=list(set(S))
  if len(T)==4:
    print("Yes")
  elif len(T)==3 or len(T)==1:
    print("No")
  else:
    if (("N" in S )and ("S" in S)) or (("W" in S) and ("E" in S)):
      print("Yes")
    else:
      print("No")
  return 

main()