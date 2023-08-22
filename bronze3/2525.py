h, m = map(int,input().split())
t = int(input())
m += t
if(m>=60):
    h += m // 60
    m %= 60
if(h>=24):
    h %= 24
print(h,m)

# 다른풀이
h, m = map(int, input().split())
s = int(input())
t=(h*60+m)+s
print(t//60%24, t%60%60)