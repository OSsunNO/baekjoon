# 내 풀이 - n의 약수를 찾기 위해 1~n으로 n을 나눠서 나머지 0 이면 리스트에 추가하고 인덱스 에러가 나면 0을 출력하는 try-except구문 활용
n,k=map(int,input().split())
a = []
for i in range(1,n+1):
    if(n%i==0):
        a.append(i)
try:
    print(a[k-1])
except IndexError:
    print(0)

# 다른 풀이 - 1 1~n으로 n을 나누는 것 까지는 동일 다만 리스트 a의 요소의 갯수가 k보다 작으면 0 출력하는 로직 사용
N ,K = map(int, input().split())
a = []
for i in range(1, N+1):
    if N%i == 0:
        a.append(i)
if (len(a)<K):
    print(0)
else:
    print(a[K-1])

# 숏코딩 - 변수 b를 생성해서 while문이 한 번 돌 때마다 b값을 1씩 추가하는 식으로 약수를 찾음 이와 동시에 b가 a의 약수라면 k를 1씩 감소시키는 방식
# while문의 조건을 k로 설정함으로써 k번째 약수를 찾으면 while구문으로부터 나옴
# 또한 k값이 전체 약수의 개수보다 많을 때(a%b만으로는 무한 루프)를 고려해 a에서 b를 뺀다는 식도 추가해서 k가 무조건 0이 될 수 있는 조건을 만듦
# 출력할 때도 b가 a보다 작거나 같을 때(b가 a의 약수일 때)만 b를 출력할 수 있게 수식을 설정
a,k=map(int,input().split())
b=0
while k:
    b+=1
    k-=((a%b)*(a-b)<1)
print(b*(a>=b))