arr = [];a,b=(0,0)
for i in range(5):
    arr.append(int(input()))
b = min(arr[3],arr[4])
a = min(arr[0],arr[1],arr[2])
print(a+b-50)