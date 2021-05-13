# B - バイナリハックイージー
def main():
    s = list(input())
    val = []

    for i in s:
        if len(val) == 0 and i == 'B':
            continue
        elif i == 'B':
            val.pop(-1)
        else:
            val.append(i)
    else:
        print(''.join(val))
 
    
if __name__ ==  "__main__":
    main()