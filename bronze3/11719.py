# import sys
# l = sys.stdin.readlines()
# for i in l:
#     print(i.rstrip('\n'))

# 다른 풀이 - open(0)으로 stdin을 파일 오브젝트로 불러오고
# read()를 통해 입력받고 이를 print()에 넣어서 출력
print(open(0).read())