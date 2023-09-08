# 내 풀이 - 입력값을 for 구문를 통해 리스트에 한 글자씩 넣음.
# 이 때, 리스트에 해당 글자가 없으면 바로 추가
# 해당 글자가 이미 있지만 바로 전 인덱스의 값과 같다면 추가 (연속된 값이기 때문)
# 그렇게 한 입력값에 대해 루프를 모두 돌았을 때 리스트에 들어간 글자 수와 입력값으로 받은 문자열의 길이가 같으면 count변수 값 1 증가

n = int(input())
count = 0
for i in range(n):
    a = []
    k = input()
    for j in k:
        if(j not in a):
            a.append(j)
        elif(j in a and a[len(a)-1]==j): a.append(j)
        else:break
    if(len(a)==len(k)):count+=1
print(count)

# 다른 풀이 - 입력값에 인덱스로 접근해서 현재 인덱스의 값과 다음 인덱스의 값이 같으면 pass(넘어감)
# 반대로 바로 뒤 인덱스값과 같지 않은데 그 후 인덱스에 포함되어 있다면 총 단어 개수값 -1
# 출력값을 처음에 입력받은 총 단어 개수 값으로 설정하면 그룹단어가 아닌 경우를 제외한 총 단어 개수가 출력
N = int(input())
gword = N
for _ in range(N):
    word=input()
    for i in range(0,len(word)-1):
        if word[i]==word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            gword-=1
            break
print(gword)
