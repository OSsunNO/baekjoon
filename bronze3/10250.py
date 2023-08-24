t = int(input())
x=0
y=0
for i in range(t):
    h,w,n = map(int,input().split())
    if(n%h==0):
        x=str(h)
        y = str(n//h)
    else:
        x=str(n%h)
        y = str(n//h + 1)
    if(len(y)==1):
        y = '0'+y
    print(x+y)

# 다른 예전 내 풀이

n = int(input())
for i in range(n):
    h,w,n = map(int,input().split())
    a = n%h
    b = n//h + 1
    if(a == 0):
        a = h
        b -= 1
    print(a*100+b)