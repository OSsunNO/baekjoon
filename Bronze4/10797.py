# 풀이 1
num = 0
n = int(input())
k = [*map(int,input().split())]
for i in range(5):
    if(k[i] == n):
        num += 1
print(num)

# 풀이 2
# num = 0
# n = input()
# k = input().split()
# for i in k:
#     if n==i:
#         num+=1
# print(num)