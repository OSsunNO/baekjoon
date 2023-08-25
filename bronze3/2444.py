n = int(input())*2
for i in range(1,n,2):
    print(' '*((n-i)//2)+'*'*i)
for j in range(n-2,0,-2):
    print(' '*((n-j)//2)+'*'*(j-1))
