S=list(input())

ans = [] #答え用意

for s in S:
  if s != 'B':
    ans.append(s) #末尾に要素追加
  elif len(ans) != 0: #長さ
    del ans[-1] #指定した位置(今回は末尾:-1)の要素を削除
    
print("".join(ans))