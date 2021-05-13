w1 = str(input())
w2 = []
for i in range(len(w1)):
    w2.append(w1[i])
from collections import Counter
w = Counter(w2).most_common()
x = 'Yes'
for h in range(len(w)):
    if w[h][1]%2 != 0:
        x = 'No'
        break
print(x)