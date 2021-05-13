#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
#方角が南北/東西でセットであればよさげ
    s = input().rstrip()
    s = set(s)
    WE={'W','E'}
    NS={'N','S'}
    all_direction={'N', 'E', 'S', 'W'}

    if s == set(WE):
        print("Yes")
    elif s == set(NS):
        print("Yes")       
    elif s == set(all_direction):
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()