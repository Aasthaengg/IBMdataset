def myAnswer(a:int,b:int) -> str:
   if(a <= 0 and b >= 0): return "Zero"
   if(a < 0):
      if(b < 0):
         return "Negative" if((abs(a-b) + 1)%2==1) else "Positive"
      else:
         return "Negative" if(abs(a)%2==1) else "Positive"
   else:
      return "Positive"


def modelAnswer():
   tmp=1
def main():
   a,b = map(int,input().split())
   print(myAnswer(a,b))

if __name__ == '__main__':
   main()