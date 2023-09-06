# 내 풀이 - 입력받은 값들을 리스트로 저장하고 for 구문을 통해 하나하나의 요소에 접근
# 두 번째 for 구문에서 1~해당요소까지 나눈 후 약수를 다른 리스트에 저장
# 이 리스트의 길이가 2 (약수가 1과 자기자신)일 때 해당 값을 최종 리스트에 저장하는 방식
n = int(input())
a = list(map(int,input().split()))
c=[]
for i in a:
    if i==1:continue
    b = []
    for j in range(1,i+1):
        if(i%j==0):b.append(j)
    if(len(b)==2):c.append(i)
print(len(c))

# 다른 풀이 - 같은 풀이인데 리스트를 하나만 만들고 count변수로 소수의 개수를 추가하는 방식
# 중간에 []와 for 구문을 통해 약수를 저장하는 리스트를 만들고 그 리스트의 len()이 2일 때 count변수의 값을 1씩 추가하는 방식임

N = input()
list1 = list(map(int,input().split()))
count = 0
for i in list1:
    if len([j for j in range(1, i+1) if i % j == 0]) == 2:
        count += 1
print(count)

# 숏코딩
int(sum(n>1for n in map(int,[*open(0)][1].split())if all(n%i for i in range(2,n))))
