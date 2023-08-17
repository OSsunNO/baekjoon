n = int(input())
for i in range(n-1,-1,-1):
    print(' '*i+'*'*(n-i))

# 이전 코드 1

# a = int(input())
# for i in range(1,a+1):
#     print((" "*(a-i)),end="")
#     print("*"*i)

# 이전 코드 2

# n = input()
# for i in range(int(n), 0 ,-1):
#     print(' ' * (i - 1), end='')
#     print('*' * (int(n) - i + 1))
