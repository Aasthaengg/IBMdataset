#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    S = input().rstrip()
    s_dict={}

    for s in S:
        if s not in s_dict:
            tmp={s:1}
            s_dict.update(tmp)
        else:
            count=s_dict[s]
            count+=1
            s_dict[s]=count
    
    for i,v in s_dict.items():
        if v % 2 !=0:
            print("No")
            exit()
        else:
            continue        
    print("Yes")
if __name__=="__main__":
    main()