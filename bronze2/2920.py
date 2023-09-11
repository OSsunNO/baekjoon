# 1~8까지 채워진 리스트를 만들어서 비교하는 방식
a = list(map(int, input().split()))
b = list(range(1,9))
if(a==b): print('ascending')
elif(a==list(reversed(b))):print('descending')
else:print('mixed')