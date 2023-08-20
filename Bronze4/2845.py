l, p = map(int,input().split())
a = list(map(int,input().split()))
for i in range(5):
    a[i] =  a[i]- l*p
print(*a)

# 다른 풀이

# a,b=map(int,input().split())
# for n in map(int,input().split()):
#     print(n-(a*b),end=' ')