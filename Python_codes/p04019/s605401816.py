def main():
    S=set(list(input()))
    flag=0
    if len(S)%2:
        flag=1
    if ('N' in S and ('W' in S or 'E' in S)) or ('S' in S and ('W' in S or 'E' in S)):
        flag=1
    if len(S)==4:
        flag=0
    print('No' if flag else 'Yes')

main()