N,L = map(int,input().split())
A = list(map(int,input().split()))

#(方針)ロープの和がある2か所でL以上ならPossible,それ以外ならImposible
#→Possibleな理由はその2か所以外から1つずつほどいていけば必ずL以上の部分ができるから
#→端からほどくとわかりやすい(?)
#→両端から行かないとL以上の部分が存在しなくなることがある

judge = 0
p1,p2 = -1,-1 #2か所で和がL以上になるところ
for i in range(N):
  if(i != N-1):
    if(A[i]+A[i+1] >= L):
      judge = 1
      p1,p2 = i,i+1
      break
point = p1+1 #p1とp2の結び目(index→問題文の数)

if(judge == 0): print('Impossible')
else:
 print('Possible')
 for i in range(1,N):
  if(i == point): break
  else: print(i)
 for i in range(1,N):
  j = N-i
  if(j == point): break
  else: print(j) 
 print(point)     