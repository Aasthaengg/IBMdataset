s_list=[int(i) for i in input().split()]

if s_list.count(5)==2 and s_list.count(7)==1:
    print("YES")
    
else:
    print("NO")