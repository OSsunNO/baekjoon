# 내 풀이 - 계산을 위한 변수 3개 설정 a는 6의 n배를 위한 용도
# b는 a의 값을 조정하기 위한 용도
# c는 중심으로부터의 거리
n=int(input())
a=1
b=1
c=2
while 1:
    if(n==1):
        print(1)
        break
    elif(n<=1+6*a):
        print(c)
        break
    b+=1
    a+=b
    c+=1

# 예전 내 풀이 - 변수 3개 설정
# 방식은 같으나 while 구문에서의 조건을 입력값이 비교값보다 클 때로 둚으로써 코드 길이 축소

a = int(input());comp=1;count=0;sum=0
while(a>comp):
    comp+=sum
    count+=1
    sum+=6
if(count==0):print(count+1)
else:print(count)