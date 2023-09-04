# 내 풀이 - 리스트 안에서 반복문을 돌려서 리스트 속 하나의 요소를 입력받은 문자열의 한 자리씩을 n번 곱한 문자열로 정의
for i in range(int(input())):
    n,s = input().split()
print(*[j*int(n) for j in s],sep='')

# 내 실수 - print()안에서 그냥 for구문을 사용하면 generator가 출력
# iterable한 객체 안에서 for구문 사용하고 그 객체의 요소에 접근해서 반환하는 방법이 맞음
# print(s[j]*int(n) for j in range(len(s)))