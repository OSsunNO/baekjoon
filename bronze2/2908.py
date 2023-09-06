# 내 풀이 - 입력받은 값에 reversed()를 적용해서 문자열 순서를 반대로 바꾼 뒤 .join()으로 하나로 합쳐줌 (reversed()의 경우 결과값이 reversed객체?이므로 join으로 합쳐줘야 함)
# 이후 map(int,~)로 각각의 입력값을 정수로 바꿔줌
# max()를 통해 거꾸로 읽은 입력값들의 최댓값 도출
n,p = input().split()
print(max(map(int,("".join(reversed(n)),"".join(reversed(p))))))

# 숏코딩 - 입력받은 값을 애초에 슬라이싱을 통해 거꾸로 만든 후 split()으로 각각의 입력값을 나눠서 리스트형태로 반환
# max()로 해당 리스트에서 최댓값 도출
print(max(input()[::-1].split()))