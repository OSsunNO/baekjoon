# 내 풀이 - 입력값을 리스트에 넣고 0 개수로 도개걸윷모 구분
for _ in range(3):
    a = [*map(int,input().split())]
    if(a.count(0)==0): print('E')
    elif(a.count(0)==1): print('A')
    elif (a.count(0)==2): print('B')
    elif (a.count(0)==3): print('C')
    else: print('D')

# 다른 풀이 - 리스트에 결과 값을 넣고 입력값들의 합을 통해 도개걸윷모 구분
A = ['D','C','B','A','E']
for _ in range(3):
    print(A[sum(map(int, input().split()))])