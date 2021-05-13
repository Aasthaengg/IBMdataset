# coding: utf-8

def main():
    S = input()
    dic = {'N':0, 'S':0, 'E':0, 'W':0}
    ans = 'No'

    for s in S:
        dic[s] += 1

    if (dic['N'] == 0 and dic['S'] == 0) or (dic['N'] > 0 and dic['S'] > 0):
        if (dic['E'] == 0 and dic['W'] == 0) or (dic['E'] > 0 and dic['W'] > 0):
            ans = 'Yes'

    print(ans)

if __name__ == "__main__":
    main()
