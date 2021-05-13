import sys
readline = sys.stdin.buffer.readline
MOD = 10**9+7

def main():
    a, b = map(int, readline().split())
    l = b-a+1
    if a<=0 and 0<=b:
        ans = 'Zero'
    else:
        if l%2==0 or 0<a:
            ans = 'Positive'
        else:
            ans = 'Negative'
    print(ans)


if __name__ == '__main__':
    main()