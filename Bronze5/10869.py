# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

import sys
a, b = map(int, sys.stdin.readline().split())
print(a+b, a-b, a*b, a//b, a%b, sep = '\n')