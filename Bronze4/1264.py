import sys
a = 'aeiouAEIOU'
lines = sys.stdin.readlines()
for line in lines:
    num = 0
    if '#' in line : break
    for i in a:
        num += line.count(i)
    print(num)


# # 다른 풀이
#
# import re
# while True:
#     k = input()
#     if k == '#':
#         break
#     else:
#         print(len(re.findall('[aeiouAEIOU]', k)))