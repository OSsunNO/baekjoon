import sys
f = sys.stdin.readlines()
for line in f:
    print(line.rstrip())

# 이전 풀이
# import sys
# for i in range(100):
#     a = sys.stdin.readline().rstrip()
#     print(a)