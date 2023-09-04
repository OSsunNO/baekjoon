import sys
ls = sys.stdin.readlines()
b=[]
c=[]
for l in ls:
    a = l.rstrip().split()
    a = list(map(int, a)) # 리스트 안 요소를 전부 int로
    b.append(max(a))
    c.append(a.index(max(a)))
print(max(b))
print(b.index(max(b))+1,c[b.index(max(b))]+1)

# 다른 풀이 - for문을 통한
l=[]
s=[]
for i in range(9):
    l.append(list(map(int,input().split())))
    s.append(max(l[i]))
q=max(s)
w=s.index(q)
print(q)
print(w+1,l[w].index(q)+1)