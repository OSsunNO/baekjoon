# 어떠한 수의 가장 큰 약수는 결국 제곱근이므로 피연산자를 제곱근까지 설정하여 나눠줌
# 원래는 리스트에 나눠질 때마다 하나씩 추가하여 리스트의 길이가 2면 출력하는 방식을 채택
# 리스트에 하나하나 추가하는 것도 n의 시간복잡도를 가지므로 생략해야 제한시간에 맞출 수 있음
# 따라서, 2번째 for구문의 조건을 2~제곱근의 수 중 나눠지는 수가 있으면 바로 break
# break 이후 하위 코드에서 break가 걸리면 생략하고 걸리지 않으면 실행시킬 수 있게하는 else의 활용법 숙지 필요
import time
s = time.time()
import sys
m,n = map(int,sys.stdin.readline().split())
for i in range(m,n+1):
    if i==1: continue
    for j in range(2,int(i**(1/2)+1)):
        if i%j==0: break
    else:print(i) # key point - break가 안걸리고 두번째 for구문이 다 돌았을 때만 실행
    # 만약, else가 없이 print(i)만 있었다면 break가 걸렸어도 i가 출력
e = time.time()
print(e-s)

# 실수 요인 - 리스트에 하나하나 append()하는 것도 n의 시간복잡도를 가지기 때문에 최대한 생략하는 코드를 짜야 제한시간 안에 들어올 수 있음
# 특히나,  break가 걸렸을 때 하위 코드를 진행하지 않고 걸리지 않았을 때만 하위 코드를 진행하는 else의 사용법 숙지 필요
import sys
m,n = map(int,sys.stdin.readline().split())
for i in range(m,n+1):
    if i==1: continue
    ar=[]
    for j in range(2,int(i**(1/2)+1)):
        if(len(ar)>2):break
        if(i%j==0):ar.append(j)
    if(len(ar)==0):print(i)