# 내 풀이 - 리스트 안에서 반복문을 돌려서 리스트 속 하나의 요소를 입력받은 문자열의 한 자리씩을 n번 곱한 문자열로 정의

# 내 실수 - print()안에서 그냥 for구문을 사용하면 generator가 출력
# iterable한 객체 안에서 for구문 사용하고 그 객체의 요소에 접근해서 반환하는 방법이 맞음
print(s[j]*int(n) for j in range(len(s)))
for i in range(int(input())):
    n,s = input().split()
    print(*[j*int(n) for j in s],sep='')

# 숏코딩 - open(0)해서 읽어들인 값들을 리스트에 넣고 unpack한 후(한 줄씩이 한 요소가 되게 하기 위해) 슬라이싱을 통해 필요한 반복횟수와 문자열만을 변수에 저장
# 이때, 문자열 역시도 unpack해줘야 함 - 안할 시 오류
# 정확한 이유는 알 수 없지만 iterator로 반환돼서 unpack을 해야만 리스트로 하나씩 저장되는 거 같음
# 이후 print() 내부에서 ''.join()과 for 구문을 통해 요소 하나하나를 여러 개로 만들어 ''로 이어붙인 뒤 출력
# .join()의 경우도 결국 iterable한 객체를 인자로 받으므로 내부에서 for구문이 사용 가능함
for r,_,*s,_ in[*open(0)][1:]:print(''.join(c*int(r)for c in s))