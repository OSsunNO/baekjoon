h,m = map(int,input().split())
m -= 45
if(m<0):
    h-=1
    m+=60
if(h<0):
    h+=24
print(h,m)

# 다른 풀이 - 분 단위로 바꾼 후 하루를 더 더해준 상태에서 연산해서 답을 구함
# a,b=map(int,input().split(' '))
# c=a*60+b+24*60-45
# a=c//60%24
# b=c%60
# print(a,b)