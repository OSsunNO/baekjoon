a = 0
for i in range(4):
    a += int(input())
x = a//60; y = a%60
print(x,y,sep='\n')