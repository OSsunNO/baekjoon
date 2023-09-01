# 65~90 A-Z 97~122 a-z
# 내 풀이
s = input()
ar = []
for i in s:
    if (65<=ord(i)<=77 or 97<=ord(i)<=109):
       ar.append(chr(ord(i)+13))
    elif (78<=ord(i)<=90 or 110<=ord(i)<=122):
        ar.append(chr(ord(i)-13))
    else:
        ar.append(i)
print(*ar,sep='')

# 다른 풀이 1 - codecs 모듈 사용
# 파이썬 파일 인코딩 변환 함수인 codecs.encode()메서드를 사용
import codecs
print(codecs.encode(input(),'rot_13'))

# 다른 풀이 2 - enumerate() 메서드와 수식 사용
# enumerate()를 통해 인덱스와 값을 동시에 for 구문 변수에 맵핑
# 이후 입력 때 받은 리스트의 인덱스에 수식을 이용해 바꾼 문자를 덮어씌움
# 수식 한 번 볼 필요 있음
a= list(input())

for i, c in enumerate(a):
  if c.isupper(): a[i]= chr(65+(ord(c)-65+13)%26)
  if c.islower(): a[i]= chr(97+(ord(c)-97+13)%26)

print(*a, sep='')