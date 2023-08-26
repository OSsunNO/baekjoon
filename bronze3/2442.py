n = int(input())
k=n-1
for i in range(1,2*n,2):
    print(' '*k+'*'*i)
    k-=1

# 다른 수식을 적용한 풀이
# n = int(input())
#
# for i in range(n):
#   print(' '*(n-1-i)+'*'*(2*i+1))