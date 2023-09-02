n = int(input())
for i in range(n):
    print(' '*i+'*'*(2*(n-i)-1))
for j in range(n-1):
    print(' '*(n-2-j)+'*'*(2*j+3))

# 다른 풀이
# 최근 추가된 := 연산자는 값을 할당하고 바로 값을 반환하기 때문에 할당과 사용을 동시에 가능
# while()구문의 조건으로 입력값-1의 절댓값을 바로 할당한 l이
# 입력값보다 작은동안 while구문 실행. 즉, 5 입력 시 m이 4~-4 l이 4~4까지 변하는 동안 총 9번 실행
# 이후 ~l과 처음에 받은 두 개의 입력값 중 식에 의해 변환되지 않는 n을 사용해 공백 개수 조정
# 이때 ~(10진수)의 경우 비트연산으로 인해 무조건 ((10진수+1)*-1)의 값이 나옴
# 또 l이 항상 양수이므로 l의 값을 이용해서 별의 개수 조정
n=m=int(input())
while(l:=abs(m:=m-1))<n:
    print(' '*(n+~l)+'*'*(l*2+1))