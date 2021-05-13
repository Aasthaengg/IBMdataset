import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    s = input()
    ans = []
    for i in range(len(s)):
        if s[i] == 'B':
            if ans:
                ans.pop()
        else:
            ans.append(s[i])
    ans = "".join(ans)
    print(ans)

if __name__ == '__main__':
    main()