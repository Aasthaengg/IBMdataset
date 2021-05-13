"""
kari1 = '4 8'
kari2 = '7 9 8 9' #5
#kari1 = '3 8'
#kari2 = '6 6 9' #0
#kari1 = '8 5'
#kari2 = '3 6 2 8 7 6 5 9' #19
#kari1 = '33 3'
#kari2 = '3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3' #8589934591
n, a = map(int, kari1.split())
x_a = list(map(lambda x: int(x) - a, kari2.split()))
"""
n, a = map(int, input().split())
x_a = list(map(lambda x: int(x) - a, input().split()))
dic = dict()
dic[0] = 1

for x in x_a:
    for key, value in list(dic.items()):
        dic[x + key] = value + dic.get(x + key, 0)

print(dic[0] - 1)
