w = input()
W = []
for i in range(len(w)):
    W.append(w[i])

W.sort()

if len(w) % 2 == 1:
    print("No")
    exit()

for i in range(len(w)//2):
    if not W[2*i] == W[2*i+1]:
        print("No")
        exit()
print("Yes")