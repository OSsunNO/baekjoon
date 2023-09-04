# 내 풀이 - 'O'가 나오면 합하는 값에 +1 함과 동시에 결과값에 합하는 값을 더해줌
# 'X'가 나오면 합하는 값을 다시 0으로 초기화해서 연속성 제거
for _ in range(int(input())):
    a = input()
    s=0
    k=0
    for i in range(len(a)):
        if(a[i]=='O'):
            s+=1
            k+=s
        else: s=0
    print(k)

# 다른 풀이 - 내 풀이에서 두번째 for문의 인자를 더 간단하게 바꾼 버전
for _ in range(int(input())):
    s = input()
    sum=0
    i=0
    for chr in s:
		if chr == 'O':
			i+=1
			sum+=i
		else:i=0
    print(sum)

# 숏코딩 - for 구문에 in에 대한 인자로 open(0)사용 이때, 인풋값을 언팩해서 리스트에 저장한 값을 인자로 사용함
# open(0)을 사용했기 때문에 처음에 받는 값을 무시하기 위해 슬라이싱 이용 - for i in [*open(0)][1:]:
# 다음 줄을 확인할 때마다 더해주는 값을 초기화하는 n=0
# 'O'가 연속해서 나올 시 가중치를 부여하는 로직을 sum()내부에 ':=' 연산자와 논리값의 곱을 사용해서 구현했으며 sum내부에서 for구문을 통해 문자열에  해당 로직 적용
# print(sum((n:=(n+1)*(j=='O'))for j in i))
for i in[*open(0)][1:]:n=0;print(sum((n:=(n+1)*(j=='O'))for j in i))