m = 0
n = 0
for i in range(9):
    k = int(input())
    if(k>m):
        m = k
        n = i+1
print(m,n,sep='\n')

# 다른풀이
print(max((int(input()),i+1) for i in range(9)))



