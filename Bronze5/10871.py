n, x = map(int, input().split())
arr = []
num = [*input().split()] # input 받자마자 공백을 기준으로 요소 받아서 리스트 생성
for i in range(n):
    if x > int(num[i]):
        arr.append(num[i])
print(*arr) # * (배열도 asterisk로 압축해제가능) 굳이 for 문으로 출력할 필요 x