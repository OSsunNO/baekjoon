n = int(input())
for i in range(n):
    print(' '*i+'*'*(2*(n-i)-1))

# 다른 풀이 - 입력값 변수 2개에 할당
# 고정된 변수 1개와 나머지 변수 1개 값의 조정으로 공백 및 별 개수 조정
k=n=int(input())
while n:print(' '*(k-n)+'*'*(2*n-1));n-=1