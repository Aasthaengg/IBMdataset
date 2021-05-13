N = int(input())*2
N -= 1
inp = input()
skewers=[]
for num in inp.split():
    skewers.append(int(num))
skewers = sorted(skewers)
total = 0
for i in range(0,N,2):
  num = int(skewers[i])
  total+=num
print(total)
