n,m = map(int,input().split())
for _ in range(n):
    t = input()
    print("".join(reversed(t)))

# 다른 풀이 - 1
# n,m = map(int,input().split())
# for _ in range(n):
#     print(input()[::-1])

# 다른 풀이 2 - 리스트에 넣고 for문 써서 반대로 출력