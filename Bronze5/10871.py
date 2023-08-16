n, x = map(int, input().split())
arr = []
for i in range(n):
    num = int(input())
    if x > num:
        arr.append(num)
print(*arr) # * (배열도 asterisk로 압축해제가능) 굳이 for 문으로 출력할 필요 x