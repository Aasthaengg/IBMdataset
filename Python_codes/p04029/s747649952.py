N = int(input())

# 1+2+3+4+...+(N-2)+(N-1)+N
# N+(N-1)+(N-2)+...+4+3+2+1
# 上と下を足し算して、２で割る

a = N+1
b = N

print(int( a * b * 0.5 ))