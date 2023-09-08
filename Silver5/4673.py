# 내 풀이 - 하드 코딩
a=[0]*10036
a[0]=1
for i in range(1,10001):
    if(len(str(i))==1): a[i+i] = 1
    elif(len(str(i))==2):a[i+i//10+i%10]=1
    elif(len(str(i))==3):a[i+i//100+i%100//10+i%10]=1
    elif(len(str(i))==4):
        a[i+(i//1000)+(i%1000//100)+(i%100//10)+i%10]=1
for j in range(1,10001):
    if(a[j]==0):
        print(j)

# 내 풀이 2 - 다른 사람 알고리즘 참고
# d(n)함수 정의 - n에 각 자리 수의 값들을 더해 return. sum()내부에서 for구문을 통해 구현
# d(n)에 해당하는 값들을 전부 리스트에 넣고 1~10000에서 해당 리스트에 없는 값들을 대조해 출력하는 방식
def d(n):
    return n + sum(int(i) for i in str(n))
a=[]
for j in range(1,10000):
    a.append(d(j))
for k in range(1,10000):
    if(k not in a):
        print(k)

# 내 풀이 3 - 다른 사람 알고리즘 참고
# set을 활용한 풀이
# set의 경우 '-'연산이 차집합으로 사용 가능
# 1~10000을 담은 set을 하나 정의하고 d(n)이 가능한 숫자들을 다른 set에 넣어서 빼는 방식으로 구현
s = set(range(1,10000))
de_set = set()
for i in s:
    for j in str(i):
        i += int(j)
    de_set.add(i)
result = s-de_set
for r in sorted(result):
    print(r)