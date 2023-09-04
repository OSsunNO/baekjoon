# 내 풀이
# 3번 입력 받아서 1에 누적해 곱한 값이 a
# a를 str()로 문자열로 만듦
# for구문을 이용해 0~9까지를 i를 통해 count함
a=1
for _ in range(3):
   a*=int(input())
b = [*str(a)]
for i in range(10):
   print(b.count(str(i)))

# 다른 풀이 - 숏코딩
# eval()을 통해 입력값끼리 곱한 후 str()로 문자열로 변환
# 문자열(리스트).count를 map()안에서 적용시킴
# count()의 매개변수를 map을 이용해 ','뒤에 한 번에 문자열로 입력
# 이후 *를 통해 unpack한 결과를 출력
print(*map(str(eval('int(input())*'*3+'1')).count,'0123456789'))
