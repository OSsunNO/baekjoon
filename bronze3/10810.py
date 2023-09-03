# 내 풀이 1
n,m = map(int,input().split())
a = [0]*n
for _ in range(m):
    i,j,k = map(int,input().split())
    for m in range(i-1,j):
        a[m]=k
print(*a)

# 내 풀이 2
n,m = map(int,input().split())
a = [0]*n
for h in range(m):
    i,j,k = map(int,input().split())
    a[i-1:j]=[k]*(j-i+1)
print(*a)

# 다른 풀이
p,_,*l=map(int,open(0).read().split())
L=[0]*p
while l:p,q,r,*l=l;L[p-1:q]=[r]*(q-p+1)
print(*L)