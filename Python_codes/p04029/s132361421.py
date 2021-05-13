#043A

#1.入力をちゃんと受け取ること
x=input()
i=int(x)
sum=0
#2.結果を出力する
while i>0:
    sum=sum+i
    i=i-1
if i==0 :
    print(sum)
