# 전부 대문자로 변환해서 입력받음
# 입력받은 값을 ord()로 바꿔 0으로 채워진 리스트에 인덱스로 맵핑하여 단어 1개당 1씩 추가
# 최댓값이 2개 이상 있으면 ?출력
# chr()을 사용해 최댓값을 가진 인덱스값을 가져와 다시 알파벳 형태로 반환
n=input().upper()
a=[0]*26
for i in range(len(n)):
    a[ord(n[i])-65]+=1
if(a.count(max(a))>1):print('?')
else:
    print(chr(a.index(max(a))+65))