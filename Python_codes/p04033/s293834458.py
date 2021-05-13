def myAnswer(a:int,b:int) -> str:
   # ゼロがまたがっている場合はzero ex)-1 2
   if(a <= 0 and b >= 0): return "Zero"
   
   if(a < 0):# aが負の数で
      if(b < 0): # bも負の数だった場合は,負の数の個数をカウントし、奇数ならNegative,偶数ならポジティブ
         return "Negative" if((abs(a-b) + 1)%2==1) else "Positive"
   else:
      return "Positive"


def modelAnswer():
   tmp=1
def main():
   a,b = map(int,input().split())
   print(myAnswer(a,b))

if __name__ == '__main__':
   main()