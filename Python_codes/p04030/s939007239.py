def main():
    s=input()
    li=[]
    for i in range(len(s)):
        if(s[i]!='B'):
            li.append(s[i])
        else:
            if(len(li)!=0):
                li.pop()
    for i in li:
        print(i,end='')

main()
