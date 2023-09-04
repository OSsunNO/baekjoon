# 내 풀이 - -1이 26개 채워진 리스트 생성(알파벳 갯수)
# 입력값에서 a~z를 찾기 위해 for구문에 ord()값과 상응하는 수를 넣어서 루프
# 입력 문자열에서 .find()와 chr()을 사용해 인덱스 값 구함
# 리스트에서 상응하는 인덱스의 값을 입력값에서 해당 알파벳이 최초 출현한 위치로 변경
# 했던 실수 - .find()는 리스트가 아닌 문자열에만 적용가능 .index()는 둘 다 가능
# chr을 통해 알파벳 변환을 해야하는데 자꾸 str()을 사용

n = input()
a=[-1]*26
for i in range(97,123):
    l = n.find(chr(i))
    a[i-97]=l
print(*a)
