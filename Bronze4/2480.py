a, b, c = map(int, input().split())
prize = 0
if(a==b==c):
    prize = 10000+a*1000
elif(a==b or a==c or b==c):
    if(a==b):
        prize = 1000+a*100
    else:
        prize = 1000+c*100
else:
    prize = max(a,b,c)*100
print(prize)

# short coding - 슬라이싱을 이용한 숏코딩 방법

# a,b,c=sorted(input().split())
# print(['1'+b,c][a<b<c]+'000'[a<c:])

#####설명#####
# - 3개 동일 -> 3개 중 아무 하나
# - 2개 중복 -> 중복된 숫자
# - 중복 X -> 가장 큰수
# ['1'+b, c][a<b<c] 이 코드에서 1은 중복된 숫자가 있을 경우 더해질 10000과 1000의 1를 뜻한다.
# 입력된 숫자가 ‘3 2 3’이면 변수에 넣어질 때 정렬이 됨으로 a = 2, b = 3, c = 3이 된다.
# 변수가 str 타입이므로 숫자 더하기가 아닌 문자 더하기으로 계산이 되기 때문에 ['1'+b, c]은 ['13', 3]이 된다.
# 그 후 중복이 있는지 없는지를 확인하였다. -> [a<b<c]는 b=c 임으로 False가 나오게 된다.
# False은 0으로 취급할 수 있기 때문에 최종 나오는 결과는 13이 나오게 된다. 만약 중복값이 없다면 a<b<c가 True가 됨으로 가장 큰 수인 C가 나오게 된다.
# 위에 중복값이 있는지 없는지를 확인하였다. 이제 각 상황에 맞게 10000의 자리인지 1000의 자리인지 100의 자리인지를 확인해야한다.
# 이는 a<c를 이용하여 확인
# 3개가 중복이면 a=c가 됨으로 False가 나오고 000이 더해지게 된다.
# 중복 2개 or 중복이 없으면, True가 나와서 00이 된다.