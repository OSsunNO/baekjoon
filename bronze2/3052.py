# 내 풀이 - 입력받은 값의 42에 대한 나머지 구함
# 해당 값이 리스트 안에 없으면 추가
# 리스트 길이 출력
a=[]
for _ in range(10):
    j = int(input())%42
    if(j not in a):a.append(j)
print(len(a))

# 예전 내 풀이 - 입력받은 값의 42에 대한 나머지 구해서 리스트에 추가
# 리스트를 set으로 변경해 중복 제거
# set의 길이 출력
b = []
for i in range(10):
    a = int(input())
    b.append(a%42)
c = set(b)
print(len(c))

# 숏코딩 - for문의 in 조건으로 open(0)을 써서 받을 만큼 받고
# 받은 요소를 i에 할당해 int(i)%42계산
# 이 모든 식을 {}안에 넣음으로써 중복 제거(set의 특징)
# 마지막으로 len()으로 감싸서 중복없이 서로 다른 값의 개수를 출력
print(len({int(i)%42for i in open(0)}))
