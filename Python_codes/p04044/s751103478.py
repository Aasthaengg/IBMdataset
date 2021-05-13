def check(s1, s2):
    for i in range(len(s1)):
        if s1[i] < s2[i]:
            return s1
        elif s1[i] > s2[i]:
            return s2
    return s1
        

def s(a, l):
    for i in range(len(a)):
        m_step = 'z' * l
        ind = -1
        for j in range(i, len(a)):
            m_step = check(m_step, a[j])
            if m_step == a[j]:
                ind = j
        a[i], a[ind] = a[ind], a[i]
    return a
        
        
            

n, l = map(int, input().split())
strs = []
for i in range(n):
    strs.append(input())
print(''.join(s(strs, l)))


