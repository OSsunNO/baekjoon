# import math
# n = input()
# if(len(n)<=10):
#     print(n)
# else:
#     for i in range(math.ceil(len(n)/10)):
#         print(n[i*10:i*10+10])

# 다른 풀이 - if문이 필요 없어 생략하기
import math
n = input()
print(*(n[i*10:i*10+10] for i in range(math.ceil(len(n)/10))),sep="\n")

# 다른 사람 풀이 - for 구문의 step attribute를 이용해서 매우 쉽게 품;
s = input()
for i in range(0, len(s), 10):
    print(s[i:i + 10])