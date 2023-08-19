# 풀이 1

print(*sorted(list(map(int,input().split()))))


# 풀이 2
# temp = []
# arr = [*map(int, input().split())]
# if(arr[2]<arr[1]):
#     temp.append(arr[1])
#     arr[1] = arr[2]
#     arr[2] = temp[0]
#     temp.pop()
# if(arr[1]<arr[0]):
#     temp.append(arr[0])
#     arr[0] = arr[1]
#     arr[1] = temp[0]
#     temp.pop()
# if(arr[2]<arr[1]):
#     temp.append(arr[1])
#     arr[1] = arr[2]
#     arr[2] = temp[0]
# print(*arr)