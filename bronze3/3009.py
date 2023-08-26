#내 풀이
x=[]
y=[]
for i in range(3):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
print(x[(x[0]==x[1])*2],y[(y[0]==y[1])*2])

# 다른 풀이 - 0으로 가득 채운 리스트에 input으로 받은 값을 인덱스로 맵핑
# 맵핑을 이차원 배열과 배열 속 for문을 활용해서 함
# i.e) for i,j in [list(map(int,input().split())) for _ in range(3)]:
# 0으로 가득 채운 리스트의 인덱스를 i,j로 가져가서 해당 인덱스의 값에 +1
# 이후 값이 1인 요소의 인덱스를 반환하면 됨 - i.e) h.index(1)
h, w = [0] * 1001, [0] * 1001
for i, j in [list(map(int, input().split())) for _ in range(3)]:
    h[i] += 1
    w[j] += 1
print(h.index(1), w.index(1))

# 다른 풀이(숏코드) - map(int,open(0).read().split())으로 stdin을 읽어서 6개의 변수로 맵핑
# 이렇게 맵핑 시 원하는 변수의 개수만큼 입력받을 수 있음
# 이후 XOR 연산자(^)를 사용해서 다른 값 하나를 도출
# 2진수가 아닌 10진수에 사용하면 값이 다른 하나의 10진수를 도출할 수 있음
# open()의 경우 0은 stdin, 1은 stdout, 2는 stderr임
a,b,c,d,e,f=map(int,open(0).read().split());print(a^c^e,b^d^f)