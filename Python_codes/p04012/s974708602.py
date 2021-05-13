#B - 美しい文字列
w = list(input())

count = [0]*26
for i in w:
    count[ord(i)-97] += 1
if all(i%2 == 0 for i in count):
    print('Yes')
else:
    print('No')