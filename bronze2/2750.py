# open(0) 관련 정리
# open(0).read()는 파일 내용 전체를 가져와 문자열로 반환
# open(0).readline()은 파일 한 줄 가져와 문자열 반환. 포인터는 다음 줄로 이동
# open(0).readlines()는 파일 전체 가져와 리스트로 반환. 각 줄은 문자열 형태로 리스트 요소에 저장
# open(0)은 파일 전체를 파일 객체로 반환. 이후 다른 함수를 통해 다른 객체로 변경해서 사용하면 됨
# i.e. list()적용 시 리스트 형태로 변하고 int()적용 시에는 문자열과 함께 입력받았던 '\n'과 같은 개행문자를 제거할 수 있음
# 단 개행문자만 있을 경우엔 제거 불가능

# 내 풀이 - open(0)으로 받은 값을 map()을 통해 int로 바꾼 후 리스트로 변경
# 첫 줄의 입력값 제외하기위해 슬라이싱하고 정렬해서 출력
print(*sorted(list(map(int,open(0)))[1:]))

# 숏코딩 - 내가 썼던 list()를 sorted()로 대체
# [open(0)]의 경우 첫 번째 값을 슬라이싱으로 제거하기 위해 사용
# 이 때, map()를 사용하기위해 *를 사용해 unpack 해야함 -  map(int,[*open(0)][1:])

print(*sorted(map(int,[*open(0)][1:])))

