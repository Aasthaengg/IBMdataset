s_lst= list(input().split())
s_lst.sort()
ans = "YES" if "".join(s_lst)=="557" else "NO"
print(ans)