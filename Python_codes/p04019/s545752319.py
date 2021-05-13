S = list(input())
dir_set = set()
for s in S:
    dir_set.add(s)

if 'N' in dir_set and 'S' in dir_set and 'W' in dir_set and 'E' in dir_set:
    ### "NSFW" 全部ある場合    
    print("Yes")
elif not 'N' in dir_set and not 'S' in dir_set and 'W' in dir_set and 'E' in dir_set:
    ### "NS" はなく "EW" が両方ある場合
    print("Yes")
elif 'N' in dir_set and 'S' in dir_set and not 'W' in dir_set and not 'E' in dir_set:
    ### "NS" が両方あり "EW" がない場合
    print("Yes")
else:
    ### 上記以外
    print("No")