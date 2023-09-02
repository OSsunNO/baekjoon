# 내 풀이
# 오차가 없게 하기 위해 math 모듈의 pi 함수(상수) 가져옴
# 출력 예제가 소수점 6자리까지 보여주고 있어서 6자리에 자르는 방법을 채택
# 소수점 표현하는 방식 3가지 존재 - round 함수, format 서식, f-string
# round 예시 - b = round(1.23456, 0) c = round(1.23456, 1) d = round(1.23456, 2)
# 출력 시 1.0, 1.2, 1.23
# format 서식 예시
# b = "format example2 : {:.2f} / {:.3f}".format(1.23456789, 3.456789)
# 출력 시 1.23 / 3.457
# 내가 채택한 건 f-string
from math import pi
n = int(input())
print(f'{n*n*pi:.6f}', f'{2*n*n:.6f}', sep='\n')

# 다른 풀이 - 출력 조건에 소수점 6자리까지 보여줘라가 아니므로 그냥 계산해서 출력해도 맞음
import math
n = int(input())
print(n*n*math.pi)
print(2*n*n)