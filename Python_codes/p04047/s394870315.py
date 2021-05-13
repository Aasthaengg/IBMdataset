N = int(input())
tmp_lst = input().split()
length_lst = []
#print(2*N)
for i in range(2*N):
#    print(tmp_lst[i])
    length_lst.append(int(tmp_lst[i]))
length_lst.sort()
 
output = 0
for i in range(0, 2*N, 2):
    output += length_lst[i]
 
print(output)