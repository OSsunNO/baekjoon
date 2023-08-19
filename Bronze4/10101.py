# 풀이 1

arr = []
for i in range(3):
    arr.append(int(input()))
if(arr[0]+arr[1]+arr[2]!=180):
    print('Error')
elif(arr[0]==arr[1]==arr[2]):
    print('Equilateral')
elif(arr[0]==arr[1] or arr[1]==arr[2] or arr[0]==arr[2]):
    print('Isosceles')
else:
    print('Scalene')

# 풀이 2

# a=int(input())
# b=int(input())
# c=int(input())
# if a+b+c!=180: print('Error')
# elif a==b==c: print('Equilateral')
# elif a==b or b==c or c==a: print('Isosceles')
# else: print('Scalene')